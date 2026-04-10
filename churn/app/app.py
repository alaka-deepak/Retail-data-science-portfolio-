from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib
from fastapi import FastAPI


app=FastAPI() # app is an instance of the class
# this decorator tells FastAPI that the function below corresponds to the path / with an operation get.
# It is the "path operation decorator".

# @app.get("/")   
# def read_root():
#     return {"message": "Welcome to the Churn Prediction API!"}
# @app.get("/train")
# async def read_message():
#     return {"message": "Training the model..."}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

