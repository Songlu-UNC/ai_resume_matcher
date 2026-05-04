# AI Resume Matcher

AI Resume Matcher is a Python and Flask web application that compares a resume with a job description. It uses natural language processing techniques, including TF-IDF vectorization, cosine similarity, keyword extraction, and gap analysis, to estimate how closely a resume matches a target role.

## Features

- Paste resume text and job description text into a web interface
- Generate a resume-job match score
- Extract important keywords from the resume and job description
- Identify matched keywords already present in the resume
- Identify missing job keywords that could be added to improve alignment
- Simple, clean web UI built with Flask, HTML, and CSS

## Tech Stack

- Python
- Flask
- scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- HTML/CSS

## Project Structure

```text
ai_resume_matcher/
├── app.py
├── requirements.txt
├── README.md
├── sample_data/
│   ├── sample_resume.txt
│   └── sample_job_description.txt
├── static/
│   └── style.css
└── templates/
    └── index.html
```

## How to Run Locally

1. Clone this repository:

```bash
git clone https://github.com/your-username/ai-resume-matcher.git
cd ai-resume-matcher
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

For Windows:

```bash
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
python app.py
```

5. Open the app in your browser:

```text
http://127.0.0.1:5000
```

## How It Works

1. The app cleans resume and job description text.
2. It converts both documents into TF-IDF vectors.
3. It calculates cosine similarity between the resume and job description.
4. It extracts frequent keywords from each text.
5. It compares job keywords against resume keywords to find matched and missing terms.

## Resume Bullet Example

- Built an AI-powered resume matching web application using Python, Flask, scikit-learn, TF-IDF vectorization, and cosine similarity to compare resumes with job descriptions and identify keyword gaps.

## Future Improvements

- Add PDF resume upload support
- Add downloadable match reports
- Use sentence embeddings for deeper semantic matching
- Add a dashboard for comparing multiple job descriptions
- Deploy the app using Render, Railway, or Heroku
