# feature ENgineering
from src.data_ingestion import load_data
import pandas as pd

def feature_engineering(df):

    # ensure required columns exist
    required_cols = [
        "HourSpendOnApp",
        "OrderCount",
        "DaySinceLastOrder",
        "CashbackAmount"
    ]

    for col in required_cols:
        if col not in df.columns:
            df[col] = 0

    # create features safely
    df["EngagementScore"] = df["HourSpendOnApp"] * df["OrderCount"]
    df["RecencyScore"] = 1 / (df["DaySinceLastOrder"] + 1)
    df["AvgOrderValue"] = df["CashbackAmount"] / (df["OrderCount"] + 1)

    return df
    # # Create new features
    # df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    # df["TenureMonths"] = df["Tenure"]
    # df["MonthlyChargesPerService"] = df["MonthlyCharges"] / (df["tenure"] + 1)

    # # Drop original columns if needed
    # # df.drop(columns=["tenure"], inplace=True)


