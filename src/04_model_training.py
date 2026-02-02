import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Load the merged dataset
data = pd.read_csv("data/05_merged_data.csv")

# Drop rows with missing target (only train requires target)
data = data.dropna(subset=["Weekly_Sales"])

# Encode ALL object (string) columns
label_enc = LabelEncoder()

for col in data.columns:
    if data[col].dtype == "object":
        print(f"Encoding column: {col}")
        data[col] = label_enc.fit_transform(data[col].astype(str))

# Drop useless columns
drop_cols = ["Date", "Store", "isHoliday_x", "isHoliday_y"]

for col in drop_cols:
    if col in data.columns:
        data = data.drop(col, axis=1)

# Define X (features) and y (target)
X = data.drop("Weekly_Sales", axis=1)
y = data["Weekly_Sales"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=20,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# Evaluate Model
preds = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, preds))

print("Model Trained Successfully!")
print(f"RMSE: {rmse:.2f}")

# Save Predictions
output = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": preds
})

output.to_csv("data/07_model_predictions.csv", index=False)
print("Predictions saved: data/07_model_predictions.csv")

# Save Model for Deployment
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/walmart_model.pkl")
print("Model saved at: model/walmart_model.pkl")