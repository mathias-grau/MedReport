import torch
from transformers import (
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    pipeline
)

device = "cuda" if torch.cuda.is_available() else "cpu"
cache_dir = "./"
model_name = "google/flan-t5-large"

# Load model and tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, cache_dir=cache_dir).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)

# Create summarization pipeline
summarizer = pipeline(
    "summarization",
    model=model,
    tokenizer=tokenizer,
    device=0 if device == "cuda" else -1,  # -1 = CPU, 0 = GPU
)

def summarize_data(raw_text, min_length=30, max_length=100, do_sample=False):
    """
    Summarize the raw text from a medical report into simpler terms for a patient.

    Args:
        raw_text (str): The medical report text to summarize.
        min_length (int): Minimum length of the summary.
        max_length (int): Maximum length of the summary.
        do_sample (bool): Whether to use sampling; False for deterministic output.

    Returns:
        str: A summarized version of the input text.
    """
    # Run the text through the summarizer
    assert isinstance(raw_text, str), "Input to summarizer must be a string."

    summary = summarizer(
        raw_text,
        min_length=min_length,
        max_length=max_length,
        do_sample=do_sample
    )
    # The pipeline returns a list of dicts with the key 'summary_text'
    return summary[0]['summary_text']