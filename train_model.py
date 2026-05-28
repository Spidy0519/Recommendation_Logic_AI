import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer

# Load CSV dataset
df = pd.read_csv("raw_skills.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Skills column
skills = df["Skills"]

# TF-IDF model
vectorizer = TfidfVectorizer()

# Train model
skill_vectors = vectorizer.fit_transform(skills)

# Save files
joblib.dump(vectorizer, "vectorizer.pkl")
joblib.dump(skill_vectors, "recommender.pkl")
joblib.dump(df, "dataset.pkl")

print("✅ Model trained successfully!")
print("✅ Files saved!")

