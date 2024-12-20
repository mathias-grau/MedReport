# Data Processing Module

**TODO** :
- Avoir les comptes rendus PDF dans `../data`
- Créer le fichier `extract_text_from_pdf.py`

## Usage

### Example Workflow
```python
from data_processing.extract_text import extract_text_from_pdf

# Extract text from a PDF
raw_text = extract_text_from_pdf("data/medical_report.pdf")

print(raw_text)
```
