import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from config import Config

_summarizer_pipeline = None

def get_summarizer_pipeline():
    """
    Chargement paresseux du modèle de résumé (singleton pattern).
    """
    global _summarizer_pipeline
    if _summarizer_pipeline is None:
        model_path = Config.SUMMARIZATION_MODEL_NAME

        tokenizer = AutoTokenizer.from_pretrained(model_path, cache_dir="./")
        model = AutoModelForCausalLM.from_pretrained(model_path, cache_dir="./").to(Config.DEVICE)

        # Correction : Ajout de pad_token_id pour éviter les erreurs d'arrêt prématuré
        tokenizer.pad_token_id = model.config.eos_token_id  

        _summarizer_pipeline = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            device=0 if Config.DEVICE == "cuda" else -1
        )

    return _summarizer_pipeline

def summarize_data(raw_text, min_new_tokens=20, max_new_tokens=200, do_sample=False):
    """
    Résume un texte médical en français.
    """
    summarizer = get_summarizer_pipeline()
    
    prompt_text = (
        "Tu es un médecin qui va résumer les résultats d'un patient. "
        "Lis attentivement le texte suivant et rédige un résumé concis, synthétique et original en français.\n\n"
        "Texte à résumer :\n\n"
        f"{raw_text}\n\n"
        "Résumé :"  # Marqueur pour extraire le résumé
        "Ce rapport indique que "
    )
    
    # Encodage du texte d'entrée
    inputs = summarizer.tokenizer(
        prompt_text, 
        return_tensors="pt", 
        truncation=True,  # Ajout de la troncature explicite
        max_length=2048  # Ajuster selon la capacité du modèle
    ).to(Config.DEVICE)


    if do_sample == True : 
        output = summarizer.model.generate(
            **inputs,
            min_new_tokens=min_new_tokens,
            max_new_tokens=max_new_tokens,
            do_sample=True,         # Active l'échantillonnage
            temperature=0.8,        # Paramètre utilisé en mode sampling
            top_p=0.95,             # Paramètre utilisé en mode sampling
            no_repeat_ngram_size=3, # Empêche la répétition de séquences de 3 tokens ou plus
            repetition_penalty=1.2, # Pénalise la répétition des tokens
            pad_token_id=summarizer.tokenizer.pad_token_id,
            eos_token_id=summarizer.tokenizer.eos_token_id,
            early_stopping=True
        )
    else :
        output = summarizer.model.generate(
            **inputs,
            min_new_tokens=min_new_tokens,
            max_new_tokens=max_new_tokens,
            do_sample=False,        # Désactive l'échantillonnage
            num_beams=4,            # Utilisation de la recherche par faisceaux
            no_repeat_ngram_size=3, # Empêche la répétition de séquences de 3 tokens ou plus
            repetition_penalty=1.2, # Pénalise la répétition des tokens
            pad_token_id=summarizer.tokenizer.pad_token_id,
            eos_token_id=summarizer.tokenizer.eos_token_id,
            early_stopping=True
        )




    # Décodage du texte généré
    generated_text = summarizer.tokenizer.decode(output[0], skip_special_tokens=True)

    # Extraction du résumé après le marqueur "Résumé :"
    if "Résumé :" in generated_text:
        summary_text = generated_text.split("Résumé :", 1)[-1].strip()
    else:
        summary_text = generated_text.strip()

    print("Résumé généré :", summary_text)  # Affiche le résultat
    return summary_text
