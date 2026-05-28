# 🎯 AI Job Recommendation System

An AI-powered Job Recommendation System that suggests relevant job roles based on user-entered skills using **TF-IDF Vectorization** and **Cosine Similarity**.

---

# 🚀 Live Demo

🌐 Frontend Live Website:
 [Demo Link](https://recommendlogicai.netlify.app/)

---

# 📌 Features

✅ Real-Time Job Recommendations
✅ Live Skill Search
✅ AI-Based Skill Matching
✅ TF-IDF Recommendation Engine
✅ Cosine Similarity Matching
✅ Flask REST API
✅ Interactive Frontend UI
✅ Automatic Suggestions While Typing

---

# 🛠 Technologies Used

| Technology          | Purpose              |
| ------------------- | -------------------- |
| Python              | Backend Development  |
| Flask               | API Server           |
| Pandas              | Dataset Handling     |
| Scikit-learn        | Machine Learning     |
| TF-IDF              | Text Vectorization   |
| Cosine Similarity   | Recommendation Logic |
| HTML/CSS/JavaScript | Frontend             |
| Joblib              | Model Storage        |

---

# 📂 Project Structure

```text
Recommendation_Logic_AI/
│
├── raw_skills.csv
├── train_model.py
├── app.py
├── index.html
│
├── vectorizer.pkl
├── recommender.pkl
├── dataset.pkl
│
├── requirements.txt
├── README.md
└── Procfile
```

---

# 📊 Dataset Format

CSV File: `raw_skills.csv`

Example:

```csv
Skills,Job_Role
python pandas sql,Data Analyst
python tensorflow ml,AI Engineer
html css javascript,Frontend Developer
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone YOUR_GITHUB_REPO_LINK
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🧠 Train Model

Run:

```bash
python train_model.py
```

Generated files:

```text
vectorizer.pkl
recommender.pkl
dataset.pkl
```

---

# ▶️ Run Backend

```bash
python app.py
```

Server runs on:

```text
http://127.0.0.1:5000
```

---

# 🌐 Run Frontend

Open:

```text
index.html
```

in browser.

---

# 🔥 How It Works

```text
User Types Skills
        ↓
Frontend Sends Request
        ↓
Flask API Receives Skills
        ↓
TF-IDF Converts Text to Vector
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
python machine learning
```

## Output

```text
AI Engineer
Machine Learning Engineer
Data Scientist
Backend Developer
```

---

# 📡 API Endpoint

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

# 🚀 Deployment

## Frontend Deployment

Deployed using:

* Netlify

## Backend Deployment

Deployed using:

* Render

---

# 🔮 Future Improvements

✅ Resume Upload
✅ Voice Search
✅ Tamil Language Support
✅ User Login System
✅ Chatbot Integration
✅ Deep Learning Recommendation Engine
✅ Database Integration
✅ Mobile Responsive UI

---

# 👨‍💻 Author

Rahuman

---

# 📄 License

This project is open-source and available for educational purposes.
