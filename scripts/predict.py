# scripts/predict.py

import pandas as pd
import pickle

def load_model():
    with open('models/trained_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

def make_predictions(data_path, output_path):
    model = load_model()
    data = pd.read_csv(data_path)
    
    features = ['recent_performance', 'consistency', 'injury_impact']
    predictions = model.predict(data[features])
    
    data['predicted_points'] = predictions
    data.to_csv(output_path, index=False)
    print(f'Predictions saved to {output_path}')

if __name__ == "__main__":
    make_predictions('data/features/2022-23_features.csv', 'data/features/2022-23_predictions.csv')
