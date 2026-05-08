from fastapi import FastAPI
from src.predict import predict
from pydantic import BaseModel

class Customer(BaseModel):
    Tenure:float
    PreferredLoginDevice:float
    CityTier:float
    WarehouseToHome:float
    PreferredPaymentMode:float
    Gender:int
    HourSpendOnApp:float
    NumberOfDeviceRegistered:float
    PreferedOrderCat:float
    SatisfactionScore:float
    MaritalStatus:float
    NumberOfAddress:float
    Complain:float
    OrderAmountHikeFromlastYear:float
    CouponUsed:float
    OrderCount:float
    DaySinceLastOrder:float
    CashbackAmount:float



app = FastAPI()

@app.get("/")
def home():
    return {"message": "Churn API running"}

@app.post("/predict")
def predict_api(data: Customer):
    result=predict(data.model_dump())
    return result