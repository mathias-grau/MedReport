from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
import re
import os

cache_dir = "./"

# If we want an English model
# model_name = "deepset/bert-base-cased-squad2"

# If we want a French model
model_name = "etalab-ia/camembert-base-squadFR-fquad-piaf"
tokenizer_name = "camembert-base"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(tokenizer_name, cache_dir=cache_dir)
model = AutoModelForQuestionAnswering.from_pretrained(model_name, cache_dir=cache_dir)

# Create the question-answering pipeline
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

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

def clean_answer(answer):
    """Cleans extracted answers (removes extra spaces, prepositions, etc.)."""
    answer = answer.strip().strip(",.")
    answer = re.sub(r"\bdans (le|la|les|l')\b", "", answer, flags=re.IGNORECASE)
    return answer.strip()

def extract_structured_data(context):
    """Extract structured data based on dynamically loaded questions."""
    questions = load_questions()
    extracted_data = {}

    for field, question in questions.items():
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