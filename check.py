import pandas as pd

# Load features data to inspect available columns
features_path = r"C:\Users\Upama Raut\OneDrive\Desktop\THesis Final\data\features\2022-23_features.csv"
data = pd.read_csv(features_path)
print(data.columns)
