# from src.data_ingestion import load_data
# from src.feature_engineering import feature_engineering
# from src.train import train_model
# from src.evaluate import evaluate_model
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split

import joblib


def train_model(df):

    X=df.drop(columns=["Churn"])
    y=df["Churn"]

    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

   #smote

    sm=SMOTE(random_state=42)
    X_train_res,y_train_res=sm.fit_resample(X_train,y_train)
    
    # Train XGBoost model
    model = XGBClassifier()
    model.fit(X_train_res, y_train_res)

    joblib.dump(model,'models/churn_model.pkl')

    return model,X_test,y_test

