# data_summarization/summarize.py
def summarize_data(parsed_info: dict) -> str:
    """
    Create a simple summary by stitching together the parsed information
    in plain language.
    """
    patient_name = parsed_info.get('patient_name', 'Unknown Patient')
    diagnosis = parsed_info.get('diagnosis', 'No Diagnosis Provided')
    meds = parsed_info.get('medications', 'No Medications Listed')

    summary = (f"Patient {patient_name} is diagnosed with {diagnosis}. "
               f"Medications prescribed: {meds}.")
    return summary


#### Test the functions
import sys
import os
# nécessaire pour importer les modules de data_preprocessing
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_preprocessing.extract_text import extract_text_from_pdf

preprocessed_text = extract_text_from_pdf("../data/exemple.pdf")
print(preprocessed_text)

from transformers import AutoTokenizer, AutoModelForCausalLM

# Path to the snapshots directory
model_dir = "./models--SumayyaAli--tiny-llama-1.1b-chat-medical/snapshots/026780c9872bd2c4f6fd1e4076252f03964d9b9f"

# check if the model is downloaded
if not os.path.exists(model_dir):
    print("Model not found. Please download the model first.")
    sys.exit(1)

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_dir)
print("Tokenizer loaded successfully.")
model = AutoModelForCausalLM.from_pretrained(model_dir)
print("Model loaded successfully.")

# Test the model
input_text = "The report from the patient's last visit is as follows: " + preprocessed_text + "You are the doctor, and you need to first summarize the information for the patient who does not understand medical jargon. Do it in simple terms."
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(**inputs)

# Decode the response
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
