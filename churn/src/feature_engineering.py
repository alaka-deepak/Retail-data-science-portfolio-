# feature ENgineering
from src.data_ingestion import load_data
import pandas as pd

df=load_data()

# feature engineering
# col=['MaritalStatus','PreferedOrderCat','Gender','PreferredPaymentMode','PreferredLoginDevice']
# le=LabelEncoder()
# for i in col:
#     data[i]=le.fit_transform(data[i])
# data[col_null]=data[col_null].fillna(data[col_null].median())
# data=data[(data['HourSpendOnApp'])!=0]
def feature_engineering(df):
    # Create new features
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TenureMonths"] = df["Tenure"]
    df["MonthlyChargesPerService"] = df["MonthlyCharges"] / (df["tenure"] + 1)

    # Drop original columns if needed
    # df.drop(columns=["tenure"], inplace=True)

    return df

df= feature_engineering(df)
