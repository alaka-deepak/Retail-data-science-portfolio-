import pandas as pd
from src.feature_engineering import feature_engineering
import joblib


model = joblib.load("models/churn_model.pkl")

FEATURES = model.get_booster().feature_names


def predict(data: dict):
    df = pd.DataFrame([data])

    # apply feature engineering
    df = feature_engineering(df)

    #  force correct columns + order
    df = df.reindex(columns=FEATURES, fill_value=0)

    prediction = model.predict(df)
    probability = model.predict_proba(df)[:, 1]

    return {
        "prediction": int(prediction[0]),
        "probability": float(probability[0])
    }