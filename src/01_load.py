import pandas as pd
from pathlib import Path

# Path
BASE_DIR = Path(__file__).resolve().parent.parent

# Define data directory path
DATA_DIR = BASE_DIR / "data"

# Load all CSV files
def load_datasets():
    train=pd.read_csv(DATA_DIR / "01_train.csv")
    test=pd.read_csv(DATA_DIR / "02_test.csv")     
    features=pd.read_csv(DATA_DIR / "03_features.csv")
    store=pd.read_csv(DATA_DIR / "04_stores.csv")

    return train, test, features, store

# Displaying shape of each dataset
if __name__ == "__main__":
    train, test, features, store = load_datasets()
    print("Datasets loaded successfully.")
    print("\n Train:",train.shape)
    print("\n Test:",test.shape)
    print("\n Features:",features.shape)    
    print("\n Store:",store.shape)
