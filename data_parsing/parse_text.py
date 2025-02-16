import re
import os

QUESTIONS_FILE = os.path.join(os.path.dirname(__file__), 'questions.txt')

def load_questions():
    """Dynamically load questions from questions.txt."""
    questions_dict = {}
    if os.path.exists(QUESTIONS_FILE):
        with open(QUESTIONS_FILE, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if ":" in line:  # Ensure valid format
                    key, value = line.split(":", 1)
                    questions_dict[key.strip()] = value.strip()
    return questions_dict

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
            extracted_data[field] = "N/A"  # Handle missing information

    return extracted_data

def parse_raw_text(raw_text: str) -> dict:
    """Parse raw text and extract structured information dynamically."""
    return extract_structured_data(raw_text)
