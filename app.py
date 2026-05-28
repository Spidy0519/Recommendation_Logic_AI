from flask import Flask, request, jsonify
from flask_cors import CORS

import joblib
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

CORS(app)

# Load files
vectorizer = joblib.load("vectorizer.pkl")
skill_vectors = joblib.load("recommender.pkl")
df = joblib.load("dataset.pkl")

df.columns = df.columns.str.strip()

@app.route('/recommend', methods=['POST'])

def recommend():

    data = request.json

    user_input = data['skills']

    # Convert input into vector
    user_vector = vectorizer.transform([user_input])

    # Similarity
    similarity = cosine_similarity(user_vector, skill_vectors)

    # Add score
    df["Similarity"] = similarity[0]

    # Filter results
    results = df[df["Similarity"] > 0.1]

    # Sort
    results = results.sort_values(
        by="Similarity",
        ascending=False
    )

    jobs = []

    for _, row in results.iterrows():

        jobs.append({

            "name": row["Job_Role"],

            "skills": row["Skills"].split(),

            "score": float(row["Similarity"])

        })

    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)

