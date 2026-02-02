import pandas as pd
from pathlib import Path

# Define th path to data files
project_root=Path(__file__).resolve().parents[1]
data_folder = project_root/"data"

# Load the datasets
train = pd.read_csv(data_folder / "01_train.csv")
features = pd.read_csv(data_folder / "03_features.csv")
stores = pd.read_csv(data_folder / "04_stores.csv")

if 'date' in features.columns:
    features.rename(columns={'date':'Date'}, inplace=True)

# Merge datasets to create one consolidated datframe
# Joining train with features and stores
df_merged = pd.merge(train, features, on=['Store','Date'])
df_merged = pd.merge(df_merged, stores, on='Store')

# Handle missing values(forward fill)
df_merged.fillna(0, inplace=True)

# Save the merged dataset as a CSV file for later use
output_path = data_folder / "05_merged_data.csv"
df_merged.to_csv(output_path, index=False)

print("Data preprocessing complete! Merged CSV saved as 05_merged_data.csv")
print("Columns:", df_merged.columns.tolist())
print(df_merged.head())
