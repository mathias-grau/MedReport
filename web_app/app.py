import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

# Import your modules
from data_preprocessing.extract_text import extract_text_from_pdf  
from data_parsing.parse_text import parse_raw_text                  
# If you have a summarization function:
from data_summarization.summarize import summarize_data

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return "No file part."
        file = request.files['file']
        if file.filename == '':
            return "No selected file."
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # 1) Preprocess/Extract text
            raw_text = extract_text_from_pdf(file_path)
            
            # 2) Parse the text
            parsed_info = parse_raw_text(raw_text)
            
            # 3) Summarize the text (optional if you have the module)
            # summary = summarize_data(parsed_info)

            # For demonstration, let's say we just store parsed_info
            return render_template('results.html',
                                   raw_text=raw_text,
                                   parsed=parsed_info)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
