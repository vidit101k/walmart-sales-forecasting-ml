import pandas as pd 
from pathlib import Path

# Path
project_root=Path(__file__).resolve().parents[1]
data_folder = project_root/"data"

# Load merged dataset
df=pd.read_csv(data_folder/"05_merged_data.csv")

# Convert Date column to datetime format
df['Date']=pd.to_datetime(df["Date"])

# Date features
df['Year']=df['Date'].dt.year
df['Month']=df['Date'].dt.month
df['Week']=df['Date'].dt.isocalendar().week
df['Day']=df['Date'].dt.day
df['DayOfWeek']=df['Date'].dt.dayofweek

# Sort for lag features
df=df.sort_values(by=['Store','Dept','Date'])

# Lag features
df['lag1']=df.groupby(['Store','Dept'])['Weekly_Sales'].shift(1)
df['lag2']=df.groupby(['Store','Dept'])['Weekly_Sales'].shift(2)
df['lag3']=df.groupby(['Store','Dept'])['Weekly_Sales'].shift(3)

# Rolling mean features
df['roll_mean_3']=df.groupby(['Store','Dept'])['Weekly_Sales'].shift(1).rolling(3).mean()
df['roll_mean_7']=df.groupby(['Store','Dept'])['Weekly_Sales'].shift(1).rolling(7).mean()

# Drop rows with missing lags/rolling values
df=df.dropna()

# Save final model ready CSV
output_path=data_folder/"06_model_ready_data.csv"
df.to_csv(output_path,index=False)

print("Feature Engineering Completed ! Saved as 06_model_ready_data.csv")
print(df.head())



