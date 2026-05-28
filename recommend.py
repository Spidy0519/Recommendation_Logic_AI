import joblib
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity

# Load saved files
vectorizer = joblib.load("vectorizer.pkl")
skill_vectors = joblib.load("recommender.pkl")
df = joblib.load("dataset.pkl")

# Remove extra spaces in columns
df.columns = df.columns.str.strip()

# User input
user_input = input("Enter your skills: ")

# Convert user skills into vector
user_vector = vectorizer.transform([user_input])

# Calculate similarity
similarity = cosine_similarity(user_vector, skill_vectors)

# Add similarity score
df["Similarity"] = (similarity[0] * 100).round(2)

# Filter matching jobs
results = df[df["Similarity"] > 10]

# Sort highest match first
results = results.sort_values(by="Similarity", ascending=False)

# Show results
print("\n🔥 Recommended Jobs:\n")

print(results[["Job_Role", "Skills", "Similarity"]])

