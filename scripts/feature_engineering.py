import pandas as pd
import os

# Directories for processed data and features
processed_dir = r"C:\Users\Upama Raut\OneDrive\Desktop\THesis Final\data\processed"
features_dir = r"C:\Users\Upama Raut\OneDrive\Desktop\THesis Final\data\features"

# Ensure the features directory exists
os.makedirs(features_dir, exist_ok=True)

def create_features(processed_dir, features_dir):
    # Load the cleaned data
    cleaned_file_path = os.path.join(processed_dir, '2022-23_clean.csv')
    data = pd.read_csv(cleaned_file_path)

    # Verify columns
    print("Available columns:", data.columns)

    # Create additional features
    data['cost'] = data['now_cost']  # Convert cost to correct format (e.g., 5.5)

    # Select relevant columns for features
    relevant_columns = [
        'first_name', 'second_name', 'club_name', 'position', 'cost'
    ]
    features = data[relevant_columns]

    # Save the features data
    features_file_path = os.path.join(features_dir, '2022-23_features.csv')
    features.to_csv(features_file_path, index=False)

    print(f"Features created and saved to {features_file_path}")

if __name__ == "__main__":
    create_features(processed_dir, features_dir)
