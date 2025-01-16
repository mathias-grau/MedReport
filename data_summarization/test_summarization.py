#### Test the functions
import sys
import os
# nécessaire pour importer les modules de data_preprocessing
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_preprocessing.extract_text import extract_text_from_pdf

print("Preprocessing text...")
raw_text = extract_text_from_pdf("./data/exemple.pdf")
print("... text preprocessed successfully.")

from summarize import summarize_data, questions_answers

# Step 1: Summarize the medical report
summary = summarize_data(raw_text)
print("Summary:", summary)

# Step 2: Answer a patient's question based on the summarized report
patient_question = "What treatment was provided to the patient?"
answer = questions_answers(patient_question, summary)
print("Answer:", answer)