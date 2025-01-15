import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
import torch

# Load a BERT model and tokenizer
model_name = "deepset/bert-base-cased-squad2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

import os 
print(os.getcwd())

# Get the list of questions for structured fields
with open('data_parsing/information.txt', 'r') as file:
    questions = file.readlines()
    questions = [line.strip() for line in questions]
    questions_dict = {}
    for question in questions:
        key, value = question.split(':')
        # remove the leading and trailing whitespaces
        key = key.strip()
        value = value.strip()
        questions_dict[key] = value

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
    return extract_structured_data(raw_text, questions_dict)


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