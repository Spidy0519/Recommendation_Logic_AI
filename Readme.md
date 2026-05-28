# 🎯 AI Job Recommendation System

An AI-based Job Recommendation System that suggests relevant job roles based on user-entered skills using **TF-IDF Vectorization** and **Cosine Similarity**.

---

# 🚀 Features

✅ Live Skill-Based Job Recommendations
✅ Real-Time Search Suggestions
✅ AI-Based Skill Matching
✅ TF-IDF Machine Learning Model
✅ Cosine Similarity Recommendation Engine
✅ Flask Backend API
✅ Interactive HTML Frontend
✅ Automatic Recommendation While Typing

---

# 🛠 Technologies Used

| Technology          | Purpose            |
| ------------------- | ------------------ |
| Python              | Backend Logic      |
| Flask               | API Server         |
| Pandas              | CSV Data Handling  |
| Scikit-learn        | Machine Learning   |
| TF-IDF              | Text Vectorization |
| Cosine Similarity   | Skill Matching     |
| HTML/CSS/JavaScript | Frontend UI        |
| Joblib              | Model Saving       |

---

# 📂 Project Structure

```text
Recommendation_Logic_AI/
│
├── raw_skills.csv
├── train_model.py
├── recommend.py
├── app.py
├── index.html
│
├── vectorizer.pkl
├── recommender.pkl
├── dataset.pkl
│
└── README.md
```

---

# 📊 Dataset Format

CSV File: `raw_skills.csv`

Example:

```csv
Skills,Job_Role
python pandas sql,Data Analyst
python tensorflow machinelearning,AI Engineer
html css javascript,Frontend Developer
```

---

# ⚙️ Installation

## 1️⃣ Clone Project

```bash
git clone <repository-url>
```

---

## 2️⃣ Install Required Libraries

```bash
pip install pandas scikit-learn flask flask-cors joblib
```

---

# 🧠 Model Training

Run:

```bash
python train_model.py
```

This will create:

```text
vectorizer.pkl
recommender.pkl
dataset.pkl
```

---

# 🔥 TF-IDF Explanation

TF-IDF converts text skills into numerical vectors.

Example:

```text
python machine learning
```

becomes:

```text
[0.32, 0.54, 0.11]
```

This allows AI models to compare skills mathematically.

---

# 📐 Cosine Similarity

Cosine Similarity calculates how similar user skills are to job skills.

| Similarity Score | Meaning      |
| ---------------- | ------------ |
| 90%              | Strong Match |
| 70%              | Good Match   |
| 40%              | Medium Match |
| 0%               | No Match     |

---

# ▶️ Running Flask Backend

Run:

```bash
python app.py
```

Server starts at:

```text
http://127.0.0.1:5000
```

---

# 🌐 Running Frontend

Open:

```text
index.html
```

in browser.

---

# 💡 How It Works

```text
User Types Skills
        ↓
JavaScript Sends Request
        ↓
Flask Receives Skills
        ↓
TF-IDF Converts Skills to Vector
        ↓
Cosine Similarity Calculates Match
        ↓
Matching Jobs Returned
        ↓
Frontend Displays Results
```

---

# 📌 Example

## User Input

```text
python
```

## Recommended Jobs

```text
AI Engineer
Python Developer
Data Scientist
Backend Developer
```

---

# 🧪 API Endpoint

## POST `/recommend`

### Request

```json
{
  "skills": "python machine learning"
}
```

### Response

```json
[
  {
    "name": "AI Engineer",
    "skills": [
      "python",
      "machinelearning",
      "tensorflow"
    ],
    "score": 0.92
  }
]
```

---

# 📈 Future Improvements

✅ Resume Upload
✅ Voice Input
✅ Tamil Language Support
✅ Chatbot Integration
✅ Deep Learning Recommendation Model
✅ User Authentication
✅ Job Description Matching
✅ Deployment on Render/Netlify

---

# 🏆 Use Cases

* Career Guidance
* Skill Analysis
* AI-Based Job Search
* Resume Screening
* Internship Recommendation
* Student Career Platforms

---

# 👨‍💻 Author

Rahuman

---

# 📄 License

This project is open-source and available for educational purposes.
