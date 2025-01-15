# Data Parsing Module

**TODO** :
- Avoir les comptes rendus PDF dans `../data`
- Avoir les fonctions de `../data_preprocessing/extract_text`
- A partir de la sortie de la fonction de `extract_text`, avoir un modèle qui est capable de donnéer des informations tabulaires

----

## Features


Ce que j'avais noté la dernière fois :
Plusieurs niveau d’informations à extraire 
- Nom
- Prénom 
- Sexe
- Date de naissance
- Indication de l’examen (pk) = motif : diagnostique ini, bilan d’extension, suspicion de récidive
- Voir ce qui a été fait dans l’examen
- qu’est ce qui a été fait ?
- Qu’est ce qui est exploré comme étage anatomique (tete, poitrine)
- Ensuite pour chacun des étages explorés ? Quels sont les structures qui sont normales ?
- Dans quels structure il y a une tumeur ou un cancer visualisable 
- Taille de la tumeur, nombre et taille des ganglions associés
- Interprétation médicale de tout ca 
- Classification TNM pour statifier le cancer (propre à chaque type de cancer)
Il faudrait réussir à faire quelque chose qui extrait ca et qui le met dans des données tabulaire

The features can be modified directly in the file information.txt.
To add a feature that will be parsed from the text, simply add a new line in this file of the form : 

Feature name: Explaination of the features in the form of a question

Example : 

Patient name: What is the patient name ?  
Structure: In which structure is the tumor ? 

## Usage

### Example Workflow
```python
from data_processing.extract_text_from_pdf import extract_text_from_pdf
from data_parsing.parse_text import parse_text

# Extract text from a PDF
raw_text = extract_text_from_pdf("data/medical_report.pdf")

features_df = parse_text(raw_text)
features_df.to_csv("data_preprocessing/preprocessed_data/medical_report_features.csv")
```
