import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
import torch

# Load a BERT model and tokenizer
model_name = "deepset/bert-base-cased-squad2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

# Define the list of questions for structured fields
questions = {
    "Patient name": "What is the patient's name?",
    "Patient age": "What is the patient's age?",
    "Location": "What is the location of the tumor?",
    "Distance from anal verge": "What is the distance of the tumor from the anal verge?",
    "Tumor length": "What is the tumor length?",
    "Mucinous": "Is the tumor mucinous?",
    "T-stage": "What is the T-stage of the tumor?",
    "Anal sphincter involvement": "Is there anal sphincter involvement?",
}

# Function to extract structured data
def extract_structured_data(context, questions):
    extracted_data = {}
    for field, question in questions.items():
        try:
            result = qa_pipeline(question=question, context=context)
            if result["score"] > 0.5:
                extracted_data[field] = result["answer"]
            else:
                extracted_data[field] = "N/A"
        except Exception as e:
            extracted_data[field] = "N/A"  # Handle missing information
    return extracted_data

def parse_raw_text(raw_text: str) -> dict:
    # Extract structured data
    return extract_structured_data(raw_text, questions)


# #### Test the functions
# import sys
# import os
# # nécessaire pour importer les modules de data_preprocessing
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from data_preprocessing.extract_text import extract_text_from_pdf

# preprocessed_text = extract_text_from_pdf("../data/exemple.pdf")
# print(preprocessed_text)
# parsed_text = parse_raw_text(preprocessed_text)
# print(parsed_text)