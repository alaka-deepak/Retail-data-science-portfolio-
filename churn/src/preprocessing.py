from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer


def get_preprocessor():

    num_cols = [
        "Tenure", "WarehouseToHome", "HourSpendOnApp",
        "OrderAmountHikeFromlastYear", "CouponUsed",
        "OrderCount", "DaySinceLastOrder", "CashbackAmount"
    ]

    cat_cols = [
        "PreferredLoginDevice", "PreferredPaymentMode",
        "Gender", "PreferedOrderCat", "MaritalStatus"
    ]

    # Numerical pipeline
    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    # Categorical pipeline
    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    # Combine
    preprocessor = ColumnTransformer([
        ("num", numeric_pipeline, num_cols),
        ("cat", categorical_pipeline, cat_cols)
    ])

    return preprocessor