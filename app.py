import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Breast Cancer Prediction API")

scaler = joblib.load("models/scaler.pkl")
model = joblib.load("models/model.pkl")

class Features(BaseModel):
    features: list[float]

@app.get("/")
def home():
    return {"message": "Breast Cancer Prediction API"}

@app.post("/predict")
def predict(data: Features):
    X = scaler.transform([data.features])
    pred = model.predict(X)[0]

    return {
        "prediction": "Malignant" if int(pred) == 1 else "Benign"
    }
