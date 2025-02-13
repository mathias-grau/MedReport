import re
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
from .qa_singleton import get_qa_pipeline

def clean_answer(answer: str) -> str:
    """
    Remove extra spaces, punctuation, or known patterns from the QA answer.
    """
    answer = answer.strip().strip(",.")
    answer = re.sub(r"\bdans (le|la|les|l')\b", "", answer, flags=re.IGNORECASE)
    return answer.strip()

def extract_structured_data(context: str, questions_dict: dict) -> dict:
    """
    Use the QA pipeline to extract structured data from text.
    """
    qa_pipeline = get_qa_pipeline()
    
    extracted_data = {}
    for field, question in questions_dict.items():
        try:
            result = qa_pipeline(question=question, context=context)
            if result["score"] > 0.5:
                extracted_data[field] = clean_answer(result["answer"])
            else:
                extracted_data[field] = "N/A"
        except Exception:
            extracted_data[field] = "N/A"
    return extracted_data

def parse_raw_text(raw_text: str) -> dict:
    """
    Extract structured data from raw text using the QA pipeline.
    """
    # Load questions
    with open('data_parsing/questions.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        questions_dict = {}
        for line in lines:
            key, value = line.split(':')
            key = key.strip()
            value = value.strip()
            questions_dict[key] = value

    # Extract structured data
    return extract_structured_data(raw_text, questions_dict)
