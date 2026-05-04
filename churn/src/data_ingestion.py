
import os
import pandas as pd

def load_data():

    folder="/Users/deepaksivas/Documents/GitHub/Retail-data-science-portfolio-/churn/data"
    filename="E Commerce Dataset.xlsx"
    file_path=os.path.join(folder, filename)
    data=pd.read_excel(file_path,sheet_name='E Comm')
    # print(data.head(5))
    # print(data.columns)
    return data

# print(load_data())

# features ='CustomerID', 'Churn', 'Tenure', 'PreferredLoginDevice', 'CityTier',
#        'WarehouseToHome', 'PreferredPaymentMode', 'Gender', 'HourSpendOnApp',
#        'NumberOfDeviceRegistered', 'PreferedOrderCat', 'SatisfactionScore',
#        'MaritalStatus', 'NumberOfAddress', 'Complain',
#        'OrderAmountHikeFromlastYear', 'CouponUsed', 'OrderCount',
#        'DaySinceLastOrder', 'CashbackAmount'