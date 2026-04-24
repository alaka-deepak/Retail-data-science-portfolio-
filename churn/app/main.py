from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("models/xgb_model.pkl")

@app.get("/")
def home():
    return {"message": "Churn API is running"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    pred = model.predict(df)
    return {"churn": int(pred[0])}