from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder


def preprocess_data(df):
    df=df.drop("CustomerID",axis=1)
    # Fill missing values

    col_null=[
        'DaySinceLastOrder',
        'OrderAmountHikeFromlastYear',
        'Tenure',
        'OrderCount',
        'CouponUsed',
        'WarehouseToHome'

    ]
    
    df[col_null]=df[col_null].fillna(df[col_null].median())
# Handle categorical nulls
    cat_cols = [
        'PreferredPaymentMode',
        'PreferedOrderCat',
        'PreferredLoginDevice',
        'MaritalStatus',
        'Gender'
    ]

    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    # 🔥 encode categorical
    le = LabelEncoder()
    for col in cat_cols:
        df[col] = le.fit_transform(df[col])

    # Remove invalid rows
    df = df[df['HourSpendOnApp'] != 0]

    df = df.dropna()

    # return df

print(preprocess_data(df))
