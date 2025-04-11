import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load the dataset
data = pd.read_csv("../dataset/career_data.csv")

# Separate features (X) and target (y)
X = data[["Math", "Science", "English", "Interest"]]
y = data["Career"]

# Encode the 'Interest' column (AI, Web, Data) into numbers
le = LabelEncoder()
X["Interest"] = le.fit_transform(X["Interest"])

# Train a Decision Tree Classifier
model = DecisionTreeClassifier()
model.fit(X, y)

# Save the model and the label encoder
joblib.dump(model, "career_model.pkl")
joblib.dump(le, "label_encoder.pkl")

print("✅ Model trained and saved as career_model.pkl")
