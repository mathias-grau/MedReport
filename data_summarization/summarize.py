from transformers import AutoTokenizer, AutoModelForCausalLM

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

# Specify the cache directory
cache_dir = "./"
# Example: FLAN-T5
model_name = "google/flan-t5-large"

# Download and save model to cache_dir
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, cache_dir=cache_dir)
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)

# Initialize summarization pipeline
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

# data_summarization/summarize.py
def summarize_data(raw_text) -> str:
    """
    Create a simple summary by stitching together the parsed information
    in plain language.
    """
    summary = summarizer(raw_text, max_length=100, min_length=5, do_sample=False)
    return summary[0]["summary_text"]
