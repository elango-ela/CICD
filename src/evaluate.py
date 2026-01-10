import pandas as pd, joblib, json, os
from sklearn.metrics import accuracy_score, roc_auc_score

model = joblib.load("models/model.pkl")
X_test = pd.read_csv("data/processed/X_test.csv")
y_test = pd.read_csv("data/processed/y_test.csv")

pred = model.predict(X_test)
prob = model.predict_proba(X_test)[:,1]

metrics = {
    "accuracy": accuracy_score(y_test, pred),
    "roc_auc": roc_auc_score(y_test, prob)
}

os.makedirs("metrics", exist_ok=True)
json.dump(metrics, open("metrics/metrics.json","w"))
