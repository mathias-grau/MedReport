# #### Test the functions
import sys
import os
from parse_text import parse_raw_text
# nécessaire pour importer les modules de data_preprocessing
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_preprocessing.extract_text import extract_text_from_pdf

preprocessed_text = extract_text_from_pdf("./data/exemple.pdf")
print(preprocessed_text)
parsed_text = parse_raw_text(preprocessed_text)
print(parsed_text)