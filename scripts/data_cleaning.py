import pandas as pd
import os

# Directories for raw and processed data
raw_dir = r"C:\Users\Upama Raut\OneDrive\Desktop\THesis Final\data\raw"
processed_dir = r"C:\Users\Upama Raut\OneDrive\Desktop\THesis Final\data\processed"

# Ensure the processed directory exists
os.makedirs(processed_dir, exist_ok=True)

def clean_data(raw_dir, processed_dir):
    # Load the raw data
    raw_file_path = os.path.join(raw_dir, '2022-23_raw.csv')
    data = pd.read_csv(raw_file_path)

    # Columns to drop
    cols_to_drop = ['minutes', 'goals_conceded', 'own_goals', 'penalties_missed', 'red_cards']

    # Drop unnecessary columns
    data.drop(columns=cols_to_drop, inplace=True)

    # Handle missing values
    data.fillna(0, inplace=True)

    # Save the cleaned data
    cleaned_file_path = os.path.join(processed_dir, '2022-23_clean.csv')
    data.to_csv(cleaned_file_path, index=False)

    print(f"Cleaned data saved to {cleaned_file_path}")

if __name__ == "__main__":
    clean_data(raw_dir, processed_dir)
