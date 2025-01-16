#### Test the functions
import sys
import os
# nécessaire pour importer les modules de data_preprocessing
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_preprocessing.extract_text import extract_text_from_pdf

print("Preprocessing text...")
preprocessed_text = extract_text_from_pdf("./data/exemple.pdf")
print("... text preprocessed successfully.")

from summarize import summarize_data

print("Summarizing data...")
summarized_data = summarize_data(preprocessed_text)
print("... data summarized successfully.")

print(summarized_data)
