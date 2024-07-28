from flask import Flask, request, render_template
import PyPDF2
import pyttsx3
import requests

app = Flask(__name__)

def extract_text_from_pdf(pdf_path):
    pdf_reader = PyPDF2.PdfFileReader(open(pdf_path, 'rb'))
    text = ""
    for page in range(pdf_reader.numPages):
        text += pdf_reader.getPage(page).extract_text()
    return text

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def download_pdf_from_url(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file.save('uploaded.pdf')
        text = extract_text_from_pdf('uploaded.pdf')
        text_to_speech(text)
        return 'File processed and audio played'

@app.route('/url', methods=['POST'])
def upload_url():
    pdf_url = request.form['url']
    download_pdf_from_url(pdf_url, 'downloaded.pdf')
    text = extract_text_from_pdf('downloaded.pdf')
    text_to_speech(text)
    return 'URL processed and audio played'

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, render_template
import PyPDF2
import pyttsx3
import requests

app = Flask(__name__)

def extract_text_from_pdf(pdf_path):
    pdf_reader = PyPDF2.PdfFileReader(open(pdf_path, 'rb'))
    text = ""
    for page in range(pdf_reader.numPages):
        text += pdf_reader.getPage(page).extract_text()
    return text

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def download_pdf_from_url(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file.save('uploaded.pdf')
        text = extract_text_from_pdf('uploaded.pdf')
        text_to_speech(text)
        return 'File processed and audio played'

@app.route('/url', methods=['POST'])
def upload_url():
    pdf_url = request.form['url']
    download_pdf_from_url(pdf_url, 'downloaded.pdf')
    text = extract_text_from_pdf('downloaded.pdf')
    text_to_speech(text)
    return 'URL processed and audio played'

if __name__ == '__main__':
    app.run(debug=True)

