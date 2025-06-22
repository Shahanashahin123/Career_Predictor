# 🎯 Career Predictor Web App

A simple, machine learning-powered web application that predicts your ideal career path based on your subject scores and personal interests.

## 🔧 Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Flask (Python)  
- **Machine Learning Model:** Decision Tree Classifier  
- **Deployment:** Render

## 📦 Features

- 🔍 Predicts suitable career options like **Web Developer**, **AI Engineer**, **Data Analyst**, and more  
- 📊 Accepts user input for subject scores and interest areas  
- 🖥️ Clean and modern UI for a smooth user experience  
- 🔗 Frontend and backend connected via **Fetch API**  

## 🚀 How It Works

1. User enters their scores and interests.
2. The data is sent to the Flask backend using a fetch request.
3. A trained Decision Tree Classifier model processes the input.
4. The predicted career path is displayed on the screen.

## 📁 Project Structure

career-predictor/
├── static/
│ ├── style.css
├── templates/
│ ├── index.html
├── app.py
├── model.pkl
├── README.md
