from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
import re

# Load a BERT model and tokenizer
# If we want a English model
model_name = "deepset/bert-base-cased-squad2"
# If we want a French model
# model_name = "etalab-ia/camembert-base-squadFR-fquad-piaf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
# We use this tokenizer for the French model (for the English model, use "deepset/bert-base-cased-squad2")
tokenizer_name = "camembert-base"
model = AutoModelForQuestionAnswering.from_pretrained(tokenizer_name)
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

# Get the list of questions for structured fields
with open('data_parsing/questions.txt', 'r') as file:
    questions = file.readlines()
    questions = [line.strip() for line in questions]
    questions_dict = {}
    for question in questions:
        key, value = question.split(':')
        # remove the leading and trailing whitespaces
        key = key.strip()
        value = value.strip()
        questions_dict[key] = value

# Function to clean the answers
def clean_answer(answer):
    # Remove extra spaces and leading/trailing punctuation
    answer = answer.strip().strip(",.")
    
    # Remove prepositions or articles (e.g., "dans le foie" -> "foie")
    answer = re.sub(r"\bdans (le|la|les|l')\b", "", answer, flags=re.IGNORECASE)
    
    # # Handle unwanted patterns (e.g., " John Doe," -> "John Doe")
    # answer = re.sub(r"\b,?\s*", "", answer).strip()

    answer = answer.strip()

    # Add more specific cleaning rules as needed
    return answer

# Function to extract structured data
def extract_structured_data(context, questions):
    extracted_data = {}
    for field, question in questions.items():
        try:
            result = qa_pipeline(question=question, context=context)
            if result["score"] > 0.5:
                extracted_data[field] = clean_answer(result["answer"])
            else:
                extracted_data[field] = "N/A"
        except Exception as e:
            extracted_data[field] = "N/A"  # Handle missing information
    return extracted_data

def parse_raw_text(raw_text: str) -> dict:
    # Extract structured data
    return extract_structured_data(raw_text, questions_dict)