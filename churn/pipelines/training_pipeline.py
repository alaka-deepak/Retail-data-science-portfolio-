from src.data_ingestion import load_data
from src.preprocessing import preprocess_data
from src.feature_engineering import feature_engineering
from src.evaluate import evaluate_model
from src.train import train_model
import joblib

def run_pipeline():
    # Load data
    df = load_data()

    # Preprocess data
    df = preprocess_data(df)

    # Feature engineering
    df = feature_engineering(df)

    # Train model
    model, X_test, y_test = train_model(df)

    # Evaluate model
    evaluate_model(model, X_test, y_test)

    joblib.dump(model, 'churn_model.pkl')

if __name__ == "__main__":
    run_pipeline()
