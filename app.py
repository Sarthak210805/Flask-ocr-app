from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import requests
import sqlite3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
OCR_API_KEY = os.getenv("OCR_API_KEY")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def init_db():
    conn = sqlite3.connect('extracted_texts.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS texts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            extracted TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('image')

        if not file or file.filename == '':
            return render_template('index.html', error='Please upload a valid image.')

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        with open(filepath, 'rb') as f:
            response = requests.post(
                'https://api.ocr.space/parse/image',
                files={'file': f},
                data={
                    'apikey': OCR_API_KEY,
                    'language': 'eng',
                    'isOverlayRequired': False
                }
            )

        result = response.json()
        if result.get("IsErroredOnProcessing"):
            error_message = result.get("ErrorMessage", ["Unknown error"])[0]
            return render_template('index.html', error=f"OCR API Error: {error_message}")

        parsed_results = result.get("ParsedResults", [])
        text = parsed_results[0]["ParsedText"] if parsed_results else "No text found."

        conn = sqlite3.connect('extracted_texts.db')
        c = conn.cursor()
        c.execute("INSERT INTO texts (filename, extracted) VALUES (?, ?)", (filename, text))
        conn.commit()
        conn.close()

        return render_template('result.html', text=text, image_url=f"/{filepath}")

    return render_template('index.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
