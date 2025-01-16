#### Test the functions
import sys
import os
# nécessaire pour importer les modules de data_preprocessing
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_preprocessing.extract_text import extract_text_from_pdf

print("Preprocessing text...")
preprocessed_text = extract_text_from_pdf("./data/exemple.pdf")
print(preprocessed_text)
print("... text preprocessed successfully.")

from transformers import AutoTokenizer, AutoModelForCausalLM

# Path to the snapshots directory
model_dir = "./models--SumayyaAli--tiny-llama-1.1b-chat-medical/snapshots/026780c9872bd2c4f6fd1e4076252f03964d9b9f"

# check if the model is downloaded
if not os.path.exists(model_dir):
    print("Model not found. Please download the model first.")
    sys.exit(1)

import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_dir)
print("Tokenizer loaded successfully.")
model = AutoModelForCausalLM.from_pretrained(model_dir).to(device)
print("Model loaded successfully.")

# Prepare input
input_text = "Le rapport du patient est : " + preprocessed_text + " Tu es le docteur, je veux que tu expliques en termes simples ce que le patient a ..."
inputs = tokenizer(input_text, return_tensors="pt").to(device)

# Generate output
outputs = model.generate(
    **inputs
)


print("Output generated successfully.")
# Decode the response
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)