---
title: MedReport  # Change this to your app's name
emoji: 🚀  # Choose any emoji
colorFrom: blue  # UI theme color start
colorTo: green  # UI theme color end
sdk: docker  # Flask is your framework
sdk_version: "2.0.3"  # Adjust to the correct version of Flask you're using
app_file: app.py  # Change if your main file has a different name
pinned: false
---


# MedReport

**MedReport** is an AI-powered application designed to process medical reports in dfferent formats (pdf, png, jpg, ...). The system extracts relevant information with powerful OCRs, parses key medical details, and generates easy-to-understand summaries for patients. This repository provides a modular and scalable pipeline for handling the entire workflow, from raw data extraction to summarization.


![Preview](data/video/gif2.gif)


---

## **Pipeline Overview**

The MedReport pipeline consists of three main stages:

1. **Data Preprocessing**: Extracts raw text from pdf file or images.
2. **Data Parsing**: Identifies and organizes key information (e.g., patient name, diagnosis, medications).
3. **Data Summarization**: Simplifies and summarizes the extracted information into patient-friendly language.

---

### **Repository Structure**

```plaintext
├── LICENSE               # Project license
├── README.md             # Main project documentation
├── data/                 # Sample data and documentation
│   ├── README.md         # Data-specific documentation
│   └── example.pdf       # Example medical report
├── data_preprocessing/   # Handles text extraction report
│   ├── README.md         # Documentation for preprocessing
│   ├── __init__.py       # Module initializer
│   ├── extract_text.py   # Extracts raw text from report
│   └── preprocessed_data/ # Directory for storing extracted text
├── data_parsing/         # Parses and extracts structured information
│   ├── README.md         # Documentation for parsing
│   ├── __init__.py       # Module initializer
│   ├── questions.txt     # Questions to get needed information
│   └── parse_text.py     # Code to parse key entities from raw text
├── data_summarization/   # Handles text summarization
│   └── README.md         # Documentation for summarization
│   └── summarize.py      # Code to summarize the text in the report
└── requirements.txt      # Python dependencies
├── app.py                # The Flask application
├── templates/
│   ├── index.html
│   └── results.html
├── static/
│   └── style.css         # (optional)
└── uploads/              # Where uploaded files are stored
````
---

## Pipeline Stages
1. Data Preprocessing

    - Purpose: Extract raw text from medical reports in any format.

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

### Extraction and Summarization Models from Hugging Face

To perform extraction and summarization, you need to install the following models from Hugging Face:

- [`etalab-ia/camembert-base-squadFR-fquad-piaf`](https://huggingface.co/etalab-ia/camembert-base-squadFR-fquad-piaf)
- [`meta-llama/Llama-3.2-3B-Instruct`](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct), which requires special permission for download.

#### 1. Authenticate with Hugging Face
Run the following command to log in with a new token from the Hugging Face website:

```bash
huggingface-cli login

```
Alternatively, check if a token is already saved on your machine:

```bash
huggingface-cli whoami
```
You can manage your Hugging Face tokens here : [Hugging Face Token](https://huggingface.co/settings/tokens)


#### Request Access to Llama-3.2-3B
You must apply for permission to download the model directly on Hugging Face: [Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)

#### Update Token Permissions
Once access is granted, update your token permissions:
- Go to Repositories permissions in your Hugging Face settings
- Search for `meta-llama/Llama-3.2-3B-Instruct` and grant the necessary permissions.

After completing these steps, you should be able to download and use the model.

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
