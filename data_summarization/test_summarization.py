#### Test the functions
import sys
import os
# nécessaire pour importer les modules de data_preprocessing
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_preprocessing.extract_text import extract_text

print("Preprocessing text...")
raw_text = extract_text("./data/exemple.pdf")
print("... text preprocessed successfully.")

from summarize import summarize_data

# Étape 1 : Créer un résumé du rapport médical
summary = summarize_data(raw_text)
print("Résumé : ", summary)