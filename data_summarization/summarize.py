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

# Initialize question-answering pipeline
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

# data_summarization/summarize.py
def summarize_data(raw_text) -> str:
    """
    Create a simple summary by stitching together the parsed information
    in plain language.
    """
    summary = summarizer(raw_text, max_length=100, min_length=5, do_sample=False)
    return summary[0]["summary_text"]

def questions_answers(patient_question, context) -> str:
    """
    Answer patient questions based on the summarized medical report.
    
    Args:
        patient_question (str): The question asked by the patient.
        context (str): The summarized medical report to use as context.
    
    Returns:
        str: The answer to the patient's question.
    """
    answer = qa_pipeline(question=patient_question, context=context)
    return answer["answer"]
