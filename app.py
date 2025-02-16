import os
import torch
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

from config import Config
from data_preprocessing.extract_text import extract_text
from data_parsing.parse_text import parse_raw_text
from data_summarization.summarize import summarize_data

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # ensures folder exists

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file:
            return "No file part."
        if file.filename == '':
            return "No selected file."
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # 1) Extract text
            raw_text = extract_text(file_path)

            # 2) Parse the text
            parsed_info = parse_raw_text(raw_text)

            # 3) Summarize the text
            summary = summarize_data(raw_text)

            # Clear the GPU cache only if needed
            if Config.DEVICE == "cuda":
                torch.cuda.empty_cache()

            return render_template(
                'results.html',
                raw_text=raw_text,
                parsed=parsed_info,
                summary=summary
            )
    return render_template('index.html')

if __name__ == '__main__':
    # By default, `debug=True` is not recommended in production
    app.run(host='0.0.0.0', port=5000, debug=False)
