# 🎯 Career Predictor Web App

A simple machine learning-powered web application that predicts your ideal career path based on your academic scores and interests.

## 👩‍💻 Created by
**Shahana Shahin**  
GitHub: [Shahanashahin123](https://github.com/Shahanashahin123)

---

## 🔧 Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Flask (Python)  
- **ML Model:** Decision Tree Classifier (trained using `train_model.py`)  
- **Deployment:** Render (or suitable platform)

---

## 📂 Project Files

| File                | Description |
|---------------------|-------------|
| `app.py`            | Main Flask backend application |
| `index.html`        | Frontend UI |
| `style.css`         | CSS for styling |
| `career_model.pkl`  | Trained Decision Tree model |
| `label_encoder.pkl` | Label encoder for target classes |
| `career_data.csv`   | Dataset used for training |
| `train_model.py`    | Script to train and save the model |
| `requirments.txt`   | Python dependencies |
| `pyvenv.cfg`        | Virtual environment config (optional)

---

## 📦 Features

- Predicts careers such as **Web Developer**, **AI Engineer**, **Data Analyst**, etc.
- Accepts user input for subject scores and area of interest.
- Clean and user-friendly UI.
- Frontend and backend connected using **Fetch API**.
- Lightweight and easy to deploy.

---

## 🚀 How to Run Locally

1. **Clone the repository**
   
   git clone https://github.com/Shahanashahin123/career-predictor.git
   cd career-predictor

2. **Create and activate virtual environment**

   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**
   
   pip install -r requirments.txt
   
4. **Run the application**

   python app.py
   
6. Open your browser and go to:
   
   http://localhost:5000

   
