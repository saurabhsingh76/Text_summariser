import os
import time
# import cv2
# import pytesseract
from flask import Flask, render_template, request, url_for
from PIL import Image
from werkzeug.utils import secure_filename

from summarizer1 import summarize

app = Flask(__name__)

# UPLOAD_FOLDER = '/static/uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    global rawtext
    start = time.time()
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        final_summary = summarize(rawtext)
        final_summary_gensim = summarize(rawtext)
        # NLTK
        final_summary_nltk = summarize(rawtext)
        # Sumy
        final_summary_sumy = summarize(rawtext)
        end = time.time()
        final_time = end - start
    return render_template('index.html', ctext=rawtext, final_summary=final_summary, final_summary_spacy=final_summary,
                           final_summary_gensim=final_summary_gensim, final_summary_nltk=final_summary_nltk,
                           final_summary_sumy=final_summary_sumy)


@app.route('/ocr', methods=['POST', 'GET'])
def upload_file():
    start = time.time()
    if request.method == "POST":
        file = request.files['file']


        final_summary = summarize(rawtext)

        final_summary_gensim ='Coming Soon'
        # NLTK
        final_summary_nltk = 'Coming Soon'
        # Sumy
        final_summary_sumy = 'Coming Soon'
        end = time.time()
        final_time = end - start
        return render_template('index.html', ctext=rawtext, final_summary=final_summary,
                               final_summary_spacy=final_summary,
                               final_summary_gensim=final_summary_gensim, final_summary_nltk=final_summary_nltk,
                               final_summary_sumy=final_summary_sumy)
        
if __name__ == "__main__":
    app.run(debug=True) 