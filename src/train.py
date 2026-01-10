import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib
import os

X_train = pd.read_csv("data/processed/X_train.csv")
y_train = pd.read_csv("data/processed/y_train.csv").values.ravel()

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

model = LogisticRegression(max_iter=2000)
model.fit(X_train, y_train)

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("Model and scaler saved to /models")
