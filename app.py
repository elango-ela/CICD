import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager

model = None
scaler = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global model, scaler
    scaler = joblib.load("models/scaler.pkl")
    model = joblib.load("models/model.pkl")
    yield   # API runs here
    # (optional cleanup when shutting down)

app = FastAPI(title="Breast Cancer Prediction API", lifespan=lifespan)

class Features(BaseModel):
    features: list[float]

@app.get("/")
def home():
    return {"message": "Breast Cancer Prediction API"}

@app.post("/predict")
def predict(data: Features):
    X = scaler.transform([data.features])
    pred = model.predict(X)[0]
    return {"prediction": "Malignant" if int(pred) == 1 else "Benign"}
