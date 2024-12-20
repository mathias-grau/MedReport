# MedReport

**MedReport** is an AI-powered application designed to process medical reports in PDF format. The system extracts relevant information, parses key medical details, and generates easy-to-understand summaries for patients. This repository provides a modular and scalable pipeline for handling the entire workflow, from raw data extraction to summarization.

---

## **Pipeline Overview**

The MedReport pipeline consists of three main stages:

1. **Data Preprocessing**: Extracts raw text from PDF files.
2. **Data Parsing**: Identifies and organizes key information (e.g., patient name, diagnosis, medications).
3. **Data Summarization**: Simplifies and summarizes the extracted information into patient-friendly language.

---

### **Repository Structure**

```plaintext
├── LICENSE               # Project license
├── README.md             # Main project documentation
├── data/                 # Sample data and documentation
│   ├── README.md         # Data-specific documentation
│   └── example.pdf       # Example medical report PDF
├── data_preprocessing/   # Handles text extraction from PDFs
│   ├── README.md         # Documentation for preprocessing
│   ├── __init__.py       # Module initializer
│   ├── extract_text.py   # Extracts raw text from PDF files
│   └── preprocessed_data/ # Directory for storing extracted text
├── data_parsing/         # Parses and extracts structured information
│   ├── README.md         # Documentation for parsing
│   ├── __init__.py       # Module initializer
│   └── parse_text.py     # Code to parse key entities from raw text
├── data_summarization/   # Handles text summarization
│   └── README.md         # Documentation for summarization
└── requirements.txt      # Python dependencies
````
----

## Pipeline Stages
1. Data Preprocessing

    - Purpose: Extract raw text from medical reports in PDF format.

2. Data Parsing

    - Purpose: Extract and structure relevant medical information from raw text.

3. Data Summarization

    - Purpose: Generate simplified and patient-friendly summaries of medical data.
