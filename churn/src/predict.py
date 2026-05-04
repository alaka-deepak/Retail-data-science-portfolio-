import pandas as pd
from src.feature_engineering import feature_engineering
import joblib
model=joblib.load('models/churn_model.pkl')

def  predict(data:dict):
    #1. Convert to dataframe
    df=pd.DataFrame([data])
    df=feature_engineering(df)
    # prediction

    prediction=model.predict(df)
    probability=model.predict_proba(df)[:,1]

    return {"prediction":int(prediction[0]),
            "probability":float(probability[0])
            }