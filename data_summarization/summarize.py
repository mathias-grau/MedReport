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
# import sys
# import os
# # nécessaire pour importer les modules de data_preprocessing
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from data_preprocessing.extract_text import extract_text_from_pdf

# preprocessed_text = extract_text_from_pdf("../data/exemple.pdf")
# print(preprocessed_text)