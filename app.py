from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
import re

app = Flask(__name__)

COMMON_STOPWORDS = {
    'a','an','and','are','as','at','be','by','for','from','has','have','in','is','it','its','of','on','or','that','the','to','was','were','with','will','you','your','we','our','this','role','job','work','team','experience','skills','ability'
}


def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z0-9+#.\s-]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def extract_keywords(text: str, top_n: int = 20):
    cleaned = clean_text(text)
    tokens = [t for t in cleaned.split() if len(t) > 2 and t not in COMMON_STOPWORDS]
    return Counter(tokens).most_common(top_n)


def calculate_match(resume_text: str, job_text: str):
    documents = [clean_text(resume_text), clean_text(job_text)]
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=1)
    tfidf_matrix = vectorizer.fit_transform(documents)
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    resume_terms = set(word for word, _ in extract_keywords(resume_text, 50))
    job_keywords = extract_keywords(job_text, 30)

    matched = []
    missing = []
    for keyword, count in job_keywords:
        if keyword in resume_terms:
            matched.append(keyword)
        else:
            missing.append(keyword)

    return {
        'score': round(score * 100, 2),
        'matched_keywords': matched[:15],
        'missing_keywords': missing[:15],
        'resume_keywords': extract_keywords(resume_text, 15),
        'job_keywords': job_keywords[:15]
    }


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    resume_text = ''
    job_text = ''

    if request.method == 'POST':
        resume_text = request.form.get('resume_text', '')
        job_text = request.form.get('job_text', '')

        if resume_text.strip() and job_text.strip():
            result = calculate_match(resume_text, job_text)

    return render_template('index.html', result=result, resume_text=resume_text, job_text=job_text)


if __name__ == '__main__':
    app.run(debug=True)
