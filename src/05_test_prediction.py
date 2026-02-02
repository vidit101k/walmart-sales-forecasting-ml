import pandas as pd
import joblib

# Load Model
model = joblib.load("model/walmart_model.pkl")
print("Model loaded successfully")

# Load Test Data
test = pd.read_csv("data/05_merged_data.csv")
print("Test data loaded")

# Drop unwanted columns (must match training)

drop_cols = ["Store", "Date", "Weekly_Sales"]
for col in drop_cols:
    if col in test.columns:
        test = test.drop(col, axis=1)

# Fix booleans (convert True/False to 0/1)

bool_cols = ["IsHoliday_x", "IsHoliday_y"]
for col in bool_cols:
    if col in test.columns:
        test[col] = test[col].astype(int)

# Encode categorical 'Type' column
# Map A,B,C → 0,1,2   (same encoding used in training)
if "Type" in test.columns:
    test["Type"] = test["Type"].map({"A": 0, "B": 1, "C": 2})

# Ensure all columns are numeric
test = test.apply(pd.to_numeric, errors='coerce')

# If any values became NaN due to unexpected strings:
test = test.fillna(0)

# Ensure correct column order matching training
train_cols = [
    'Dept', 'IsHoliday_x', 'Temperature', 'Fuel_Price', 'MarkDown1',
    'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5', 'CPI',
    'Unemployment', 'IsHoliday_y', 'Type', 'Size'
]

test = test[train_cols]

# Predict
preds = model.predict(test)

# Save Output
output = pd.DataFrame({"Predicted_Weekly_Sales": preds})
output.to_csv("data/08_test_predictions.csv", index=False)

print("Predictions saved to data/08_test_predictions.csv")