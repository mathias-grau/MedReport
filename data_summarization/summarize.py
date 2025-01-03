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