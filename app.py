import os
import torch
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

from config import Config
from data_preprocessing.extract_text import extract_text
from data_parsing.parse_text import parse_raw_text, load_questions
from data_summarization.summarize import summarize_data

BASE_DIR = os.path.dirname(__file__)  # MedReport/app.py
ROOT_DIR = os.path.dirname(BASE_DIR)  # MedReport/
UPLOAD_FOLDER = os.path.join(ROOT_DIR, 'uploads')
QUESTIONS_FILE = os.path.join(ROOT_DIR, 'MedReport', 'data_parsing', 'questions.txt')

os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # ensures folder exists

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Handle file upload
        if 'file' in request.files:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filename)

                # Extract raw text
                raw_text = extract_text(filename)
                
                # Parse extracted text
                parsed_info = parse_raw_text(raw_text)

                # Summarize text
                summary = summarize_data(raw_text)

                return render_template('results.html', raw_text=raw_text, parsed=parsed_info, summary=summary)

        # Handle adding new questions dynamically
        elif 'new_question' in request.form and 'field_name' in request.form:
            field_name = request.form['field_name'].strip()
            new_question = request.form['new_question'].strip()
            
            if field_name and new_question:
                with open(QUESTIONS_FILE, 'a', encoding='utf-8') as f:
                    # Ensure new question starts on a new line
                    if os.path.getsize(QUESTIONS_FILE) > 0:
                        f.write("\n")
                    f.write(f"{field_name}: {new_question}")

            return redirect(url_for('upload_file'))

    # Load current questions dynamically
    questions = load_questions()
    return render_template('index.html', questions=questions)

@app.route('/questions', methods=['GET'])
def get_questions():
    """Fetch the current questions."""
    questions = load_questions()
    print("Questions loaded:", questions)  # Debugging line
    return jsonify(questions)

@app.route('/delete_question', methods=['POST'])
def delete_question():
    data = request.get_json()
    field = data.get('field')
    question = data.get('question')

    if field and question:
        # Load current questions from file
        questions = load_questions()

        # Remove the question from the dictionary
        if field in questions and questions[field] == question:
            del questions[field]
            
            # Rewrite the questions to the file
            with open(QUESTIONS_FILE, 'w', encoding='utf-8') as file:
                for field, question in questions.items():
                    file.write(f"{field}: {question}\n")
            
            return jsonify({"message": "Question deleted successfully"})
    
    return jsonify({"message": "Error deleting question"})

if __name__ == '__main__':
    app.run(debug=True)