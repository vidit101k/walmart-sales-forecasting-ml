# 🛒 Walmart Sales Forecasting using Machine Learning

## 📌 Project Overview

Retail businesses like Walmart face significant challenges in accurately forecasting weekly sales due to seasonality, holidays, economic factors, and store-level variations.
This project aims to *predict weekly sales for Walmart stores and departments* using historical data and machine learning techniques to support *better demand planning and decision-making*.

The solution follows a *complete end-to-end Data Science pipeline*, from data preprocessing and feature engineering to model training, evaluation, and prediction.

---

## 🎯 Business Problem

Accurate sales forecasting helps retailers:

* Optimize inventory management
* Reduce stock-outs and overstocking
* Improve workforce and supply chain planning
* Maximize revenue during peak seasons and holidays

This project focuses on *forecasting weekly sales at the department level* using historical and external features.

---

## 🧠 Approach & Methodology

### 1️⃣ Data Collection

The dataset includes:

* Historical weekly sales data
* Store and department information
* Economic indicators (CPI, Unemployment)
* Fuel prices
* Holiday and promotional markdown data

---

### 2️⃣ Data Preprocessing

* Merged multiple datasets into a single structured dataset
* Handled missing values
* Removed irrelevant and identifier-based columns
* Converted categorical variables into numerical format
* Ensured consistency between training and test datasets

---

### 3️⃣ Feature Engineering

To capture time-based sales patterns, advanced features were engineered:

* *Lag Features* (previous weeks’ sales)
* *Rolling Mean Features* (moving averages)
* Holiday indicators
* Economic and promotional variables

These features help the model understand *temporal trends and seasonality*.

---

### 4️⃣ Model Training

* Model Used: *Random Forest Regressor*
* Reason:

  * Handles non-linear relationships
  * Robust to outliers
  * Performs well on structured tabular data

---

### 5️⃣ Model Evaluation

* Evaluation Metric: *Root Mean Squared Error (RMSE)*
* Achieved RMSE: *~5229*
* The model demonstrates strong predictive capability given the scale and variability of retail sales data.

---

### 6️⃣ Predictions & Model Saving

* Generated predictions on test data
* Saved results as CSV for further analysis
* Persisted trained model using joblib for deployment or future inference

---

## 🛠️ Tech Stack

* *Programming Language:* Python
* *Libraries & Tools:*

  * pandas
  * numpy
  * scikit-learn
  * joblib
* *Model:* Random Forest Regressor
* *Version Control:* Git & GitHub

---

## 📂 Project Structure


Walmart-Sales-Forecasting/
│
├── data/
│   ├── 01_train.csv
│   ├── 02_test.csv
│   ├── 03_features.csv
│   ├── 04_stores.csv
│   ├── 05_merged_data.csv
│   ├── 06_model_ready_data.csv
│   ├── 07_model_predictions.csv
│   ├── 08_test_predictions.csv
│
├── src/
│   ├── 01_load.py
│   ├── 02_data_preprocessing.py
│   ├── 03_feature_engineering.py
│   ├── 04_model_training.py
│   ├── 05_test_prediction.py
│
├── model/
│   └── walmart_model.pkl
│
├── README.md
└── requirements.txt


---

## 📈 Results & Insights

* The model successfully captures sales trends influenced by:

  * Seasonality
  * Holidays
  * Economic indicators
* Lag and rolling features significantly improved forecasting accuracy
* The solution can be extended for real-time forecasting and dashboard integration

---

## 🚀 Future Enhancements

* Hyperparameter tuning for improved accuracy
* Try advanced models (XGBoost, LightGBM)
* Store-level and department-level segmentation models
* Integration with Power BI / Tableau dashboards
* Deployment as a REST API

---

## 👤 Author

*Vidit Kajvilkar*
Aspiring Data Scientist | Machine Learning Enthusiast

---

## 📌 Key Skills Demonstrated

* Data Cleaning & Preprocessing
* Feature Engineering (Time Series)
* Machine Learning Modeling
* Model Evaluation
* End-to-End Project Implementation

---

