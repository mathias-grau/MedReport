from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
from config import Config

_qa_pipeline = None

def get_qa_pipeline():
    """
    This function returns a singleton QA pipeline, loaded once at startup.
    """
    global _qa_pipeline
    if _qa_pipeline is None:
        print("Loading QA model and tokenizer into memory...")
        tokenizer = AutoTokenizer.from_pretrained(Config.TOKENIZER_NAME, cache_dir='./')
        model = AutoModelForQuestionAnswering.from_pretrained(Config.QA_MODEL_NAME, cache_dir='./').to(Config.DEVICE)
        _qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer, device=0 if Config.DEVICE == "cuda" else -1)
    return _qa_pipeline
