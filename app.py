from flask import Flask, render_template, request, redirect
import os

from resume_parser import parse_resume
from job_matcher import get_job_match_score
import nltk
nltk.download('stopwords')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        resume_file = request.files['resume']
        job_profile = request.form['job_profile']

        UPLOAD_FOLDER = 'static/uploads'
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        filepath = os.path.join(UPLOAD_FOLDER, resume_file.filename)
        resume_file.save(filepath)

        resume_data = parse_resume(filepath)
        match_results = get_job_match_score(resume_data, job_profile)

        return render_template('result.html', resume_data=resume_data, match_results=match_results)

    return render_template('index.html')

@app.route('/suggest', methods=['POST'])
def suggest():
    suggestion = request.form['suggestion']
    with open('suggestions.txt', 'a', encoding='utf-8') as file:
        file.write(suggestion + '\n---\n')
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug=True)
