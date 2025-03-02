#### Test the functions
import sys
import os
# nécessaire pour importer les modules de data_preprocessing
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_preprocessing.extract_text import extract_text

print("Preprocessing text...")
raw_text = extract_text("./data/exemple.pdf")
print("... text preprocessed successfully.")

from summarize import ask_question_about_report

question = """Le plus précisement possible et sans phrase, répond sous forme de bullet point :
- Quel est le prénom du patient, si fourni, sinon répondre "Non fourni" ?
- Quel est le nom du patient, si fourni, sinon répondre "Non fourni" ?
- Quel est l'âge du patient, si fourni, sinon répondre "Non fourni" ?
- Quel est le type de scanner, s'il y en a un, sinon répondre "Non fourni" ?
- Quelle est le danger de 1 à 10, 10 étant le plus dangereux ?
- Quelle est la taille de la tumeur, s'il y en a une, sinon répondre "Non fourni" ?
- Quelle est la localisation de la tumeur, s'il y en a une, sinon répondre "Non fourni" ?
"""

answer = ask_question_about_report(question, raw_text)
print("Réponse générée :", answer)