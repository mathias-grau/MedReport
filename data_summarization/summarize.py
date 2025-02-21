import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from config import Config

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
                   max_new_tokens=120, 
                   do_sample=False):
    """
    Résume un texte médical en français.
    """
    summarizer = get_summarizer_pipeline()
    
    # Construire le prompt au format Instruct
    prompt_text = (
        "Below is an instruction that describes a task, paired with an input that provides further context.\n"
        "Write a response that appropriately completes the request.\n\n"
        "### Instruction:\n"
        "Tu es un médecin qui va résumer les résultats d'un patient. "
        "Rédige un résumé concis et synthétique en français.\n\n"
        "### Input:\n"
        f"{raw_text}\n\n"
        "### Response:\n"
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
        output = summarizer.model.generate(
            **inputs,
            min_new_tokens=min_new_tokens,
            max_new_tokens=max_new_tokens,
            do_sample=False,
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
    split_marker = "### Response:"
    if split_marker in generated_text:
        summary_text = generated_text.split(split_marker, 1)[-1].strip()
    else:
        summary_text = generated_text.strip()

    print("Résumé généré :", summary_text)
    return summary_text
