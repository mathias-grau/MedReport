import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from config import Config

from transformers import StoppingCriteria, StoppingCriteriaList

class StopOnSequence(StoppingCriteria):
    def __init__(self, stop_ids):
        self.stop_ids = stop_ids

    def __call__(self, input_ids, scores, **kwargs):
        # We only check the last few tokens, length of stop_ids
        if len(input_ids[0]) < len(self.stop_ids):
            return False
        # Compare trailing tokens with stop_ids
        if all(input_ids[0][-len(self.stop_ids)+i] == self.stop_ids[i] 
               for i in range(len(self.stop_ids))):
            return True
        return False


_summarizer_pipeline = None

def get_summarizer_pipeline():
    global _summarizer_pipeline
    if _summarizer_pipeline is None:
        model_path = Config.SUMMARIZATION_MODEL_NAME

        tokenizer = AutoTokenizer.from_pretrained(model_path, cache_dir="./")
        model = AutoModelForCausalLM.from_pretrained(model_path, cache_dir="./").to(Config.DEVICE)

        # Correction: Set pad_token to eos_token, then set pad_token_id
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id

        _summarizer_pipeline = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            device=0 if Config.DEVICE == "cuda" else -1
        )

    return _summarizer_pipeline


def summarize_data(raw_text, 
                   min_new_tokens=20, 
                   max_new_tokens=300, 
                   do_sample=False):
    """
    Résume un texte médical en français.
    """
    summarizer = get_summarizer_pipeline()
    
    # Construire le prompt au format Instruct
    prompt_text = (
        "### Instruction :\n"
        "Tu es un médecin qui va résumer les résultats d'un patient de manière claire et synthétique.\n\n"
        "### Texte du rapport :\n"
        f"{raw_text}\n\n"
        "### Résumé :\n"
    )
    
    # Préparer les données d'entrée
    inputs = summarizer.tokenizer(
        prompt_text, 
        return_tensors="pt", 
        truncation=True,
        max_length=2048
    ).to(Config.DEVICE)

    # Choix des paramètres de génération
    if do_sample:
        output = summarizer.model.generate(
            **inputs,
            min_new_tokens=min_new_tokens,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.8,
            top_p=0.95,
            no_repeat_ngram_size=3,
            repetition_penalty=1.2,
            pad_token_id=summarizer.tokenizer.pad_token_id,
            eos_token_id=summarizer.tokenizer.eos_token_id,
            early_stopping=True
        )
    else:
        stop_ids = summarizer.tokenizer.encode("### End", add_special_tokens=False)
        stopping_criteria = StoppingCriteriaList([StopOnSequence(stop_ids)])

        output = summarizer.model.generate(
            **inputs,
            max_new_tokens=300,
            do_sample=False,
            num_beams=4,
            stopping_criteria=stopping_criteria,
            pad_token_id=summarizer.tokenizer.pad_token_id,
            eos_token_id=summarizer.tokenizer.eos_token_id,
            early_stopping=True
        )


    # Décodage
    generated_text = summarizer.tokenizer.decode(output[0], skip_special_tokens=True)
    
    # Extraire la partie après '### Response:'
    split_marker = "### Résumé :\n"
    if split_marker in generated_text:
        summary_text = generated_text.split(split_marker, 1)[-1].strip()
    else:
        summary_text = generated_text.strip()

    print("Résumé généré :", summary_text)
    # Strip last sentence if it is incomplete and does not finish with a period
    if summary_text[-1] not in [".", "!", "?"]:
        summary_text = summary_text.rsplit(".", 1)[0] + "."
    return summary_text


def ask_question_about_report(question, raw_text):
    """
    Pose une question sur un texte médical en français.
    """
    summarizer = get_summarizer_pipeline()
    
    # poser une question sur le texte
    prompt_text = (
        "Voici un rapport : \n\n"
        f"{raw_text}\n\n"
        "### Question:\n"
        f"{question}\n\n"
    )
    
    # Préparer les données d'entrée
    inputs = summarizer.tokenizer(
        prompt_text, 
        return_tensors="pt", 
        truncation=True,
        max_length=2048
    ).to(Config.DEVICE)

    # Générer une réponse
    output = summarizer.model.generate(
        **inputs,
        max_new_tokens=200,     # on génère jusqu’à 200 tokens supplémentaires
        do_sample=False,        # beam search et pas d’échantillonnage
        num_beams=4,
        no_repeat_ngram_size=3,
        repetition_penalty=1.2,
        pad_token_id=summarizer.tokenizer.pad_token_id,
        eos_token_id=summarizer.tokenizer.eos_token_id,
        early_stopping=True
    )



    # Décodage
    generated_text = summarizer.tokenizer.decode(output[0], skip_special_tokens=True)

    # Extraire la partie après '### Response:'
    split_marker = prompt_text
    if split_marker in generated_text:
        answer_text = generated_text.split(split_marker, 1)[-1].strip()
    else:
        answer_text = generated_text.strip()

    print("Réponse générée :", answer_text)
    return answer_text
