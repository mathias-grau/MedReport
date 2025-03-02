# MedReport

**MedReport** is an AI-powered application designed to process medical reports in PDF format. The system extracts relevant information, parses key medical details, and generates easy-to-understand summaries for patients. This repository provides a modular and scalable pipeline for handling the entire workflow, from raw data extraction to summarization.

[![Watch the video](https://img.youtube.com/vi/dQw4w9WgXcQ/0.jpg)](https://github.com/mathias-grau/MedReport/tree/main/data/video/exemple_video_rapport.mov)


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
│   ├── questions.txt     # Questions to get needed information
│   └── parse_text.py     # Code to parse key entities from raw text
├── data_summarization/   # Handles text summarization
│   └── README.md         # Documentation for summarization
│   └── summarize.py      # Code to summarize the text in the PDF file
└── requirements.txt      # Python dependencies
├── app.py             # The Flask application
├── templates/
│   ├── index.html
│   └── results.html
├── static/
│   └── style.css       # (optional)
└── uploads/            # Where uploaded files are stored
````
---

## Pipeline Stages
1. Data Preprocessing

    - Purpose: Extract raw text from medical reports in PDF format.

2. Data Parsing

    - Purpose: Extract and structure relevant medical information from raw text.

3. Data Summarization

    - Purpose: Generate simplified and patient-friendly summaries of medical data.

---

## Set Up

### Environment

To run the files, one should need an environement : 

```bash
python -m venv venv
```

Then you will need to activate it : 
```bash
# Linux / Mac
source venv/bin/activate
# deactivate # to deactivate the env


# On Windows : 
venv\Scripts\activate
# venv\Scripts\deactivate # to deactivate the env
```

---

### Dependancies

Run : 
```bash
pip install -r requirements.txt
```
---

## Pipeline 

To test the full pipeline : 
```bash
chmod +x pipeline.sh
./pipeline.sh
```

---

### Tests

To test the OCR : 
```bash
cat uploads/exemple.pdf | markitdown
```
---
### Webapp 

```bash
python -m app
```


if everything is working correctly ; 

```csharp
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 121-384-574
```
