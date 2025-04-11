from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)


# Load the model and label encoder
model = joblib.load("career_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

@app.route('/')
def home():
    return "Career Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    # Extract input values
    math = data.get("Math")
    science = data.get("Science")
    english = data.get("English")
    interest = data.get("Interest")
    
    # Encode interest using label encoder
    interest_encoded = label_encoder.transform([interest])[0]
    
    # Prepare input for model
    input_df = pd.DataFrame([[math, science, english, interest_encoded]],
                            columns=["Math", "Science", "English", "Interest"])
    
    # Make prediction
    prediction = model.predict(input_df)[0]
    
    return jsonify({"predicted_career": prediction})

if __name__ == '__main__':
    app.run(debug=True)
