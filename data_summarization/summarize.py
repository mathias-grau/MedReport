import torch
from transformers import (
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    pipeline
)
from config import Config

_summarizer_pipeline = None

def get_summarizer_pipeline():
    """
    Lazily load the summarization model/pipeline only once (singleton pattern).
    """
    global _summarizer_pipeline
    if _summarizer_pipeline is None:
        print("Loading Summarization model into memory...")
        tokenizer = AutoTokenizer.from_pretrained(
            Config.SUMMARIZATION_MODEL_NAME,
            cache_dir='./'
        )
        model = AutoModelForSeq2SeqLM.from_pretrained(
            Config.SUMMARIZATION_MODEL_NAME,
            cache_dir='./'
        ).to(Config.DEVICE)
        _summarizer_pipeline = pipeline(
            "summarization",
            model=model,
            tokenizer=tokenizer,
            device=0 if Config.DEVICE == "cuda" else -1
        )
    return _summarizer_pipeline

def summarize_data(raw_text, min_length=30, max_length=100, do_sample=False, num_beams=4):
    """
    Summarize the raw text (in French) using facebook/bart-large-cnn.
    NOTE: The BART CNN model is primarily trained on English data,
    so results for French might not be perfect.

    :param raw_text: The French text you want summarized.
    :param min_length: The minimum length of the summary.
    :param max_length: The maximum length of the summary.
    :param do_sample: Whether to use sampling for text generation.
    :param num_beams: Number of beams for beam search (default=4).
    :return: A summarized string.
    """
    summarizer = get_summarizer_pipeline()

    # Provide a prompt or instruction in French
    prompt_text = f"Résumez ce texte en français :\n\n{raw_text}"

    summary = summarizer(
        prompt_text,
        min_length=min_length,
        max_length=max_length,
        do_sample=do_sample,
        num_beams=num_beams
    )
    return summary[0]['summary_text']
