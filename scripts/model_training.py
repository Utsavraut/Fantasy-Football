import pandas as pd
import os
import joblib
from sklearn.ensemble import RandomForestRegressor

# Paths for data
features_path = r"C:\Users\Upama Raut\OneDrive\Desktop\THesis Final\data\features\2022-23_features.csv"
model_path = r"C:\Users\Upama Raut\OneDrive\Desktop\THesis Final\models\trained_model.pkl"

def train_model(features_path, model_path):
    # Load the features data
    data = pd.read_csv(features_path)
    
    # Extract numerical features for training
    features = data[['cost']]
    target = features['cost']  # Dummy target as we are not using actual points

    # Handle missing values
    features.fillna(0, inplace=True)
    
    # Train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(features, target)
    
    # Save the trained model
    joblib.dump(model, model_path)
    print(f"Model trained and saved to {model_path}")

if __name__ == "__main__":
    train_model(features_path, model_path)
