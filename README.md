# Airline Passenger Satisfaction Prediction System 😌  

## 🙂 Overview

This project focuses on predicting passenger satisfaction in the aviation and customer experience domain. By analyzing passenger demographics, travel details, service ratings, and flight experience attributes, I built a machine learning classification model to identify satisfied and dissatisfied airline passengers.

*The goal is to help airlines improve service quality, identify passenger pain points, support data-driven decisions, and strengthen overall customer satisfaction and loyalty.*
 
-----

## 💡 Problem Statement & Business Impact

* Airlines collect thousands of passenger feedback records and service ratings, making it difficult to identify dissatisfied customers manually.
* Poor service experiences can reduce passenger loyalty, damage brand reputation, and increase the risk of customer dissatisfaction.
* Passenger satisfaction varies based on factors such as seat comfort, in-flight services, departure and arrival delays, travel class, and overall flight experience.
* **Goal:** Develop a classification model that predicts passenger satisfaction (Satisfied or Neutral/Dissatisfied) using demographic, travel, service rating, and flight experience attributes.
* **Business value:** Identifying dissatisfied passengers helps airlines recognize service gaps, prioritize improvements, enable proactive customer engagement, enhance passenger experience, and strengthen long-term customer loyalty.

-----

## 📂 Folder Structure

```text
Airline-Passenger-Satisfaction-Prediction-System
│
├── data
│   ├── train.csv
│   ├── test.csv
│   └── processed_data.csv
│
├── notebooks
│   ├── 1.EDA_&_Data_Preparation.ipynb
│   └── 2.Model Training & Evaluation.ipynb
│
├── models
│   └── passenger_satisfaction_model.pkl
│
├── app.py
├── .gitignore   
├── LICENSE
├── README.md
└── requirements.txt

```

-----

## 📊 Data Overview

![Airline Passenger Satisfaction](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction)

* Dataset Size: 103,904 records
* Features: 26 input variables
* Target Variable: satisfaction: `neutral or dissatisfied': 0` & `satisfied': 1`

### Key Features
* Passenger demographics
* Flight distance & travel class
* Wi-Fi, seat comfort, cleanliness
* Online booking & boarding experience
* Delay-related metrics

### Engineered Features
* Total Delay
* Delayed Flight
* Average Service Rating
* Long Haul Indicator

---

## 🔄 End-to-End Workflow & Approach
1. Data Collection & Understanding
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Train-Test Split
6. Model Training
7. Hyperparameter Tuning
8. Performance Evaluation
9. Model Serialization
10. Streamlit Deployment

---

## 🛠️ Tech Stack
* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-Learn
* Streamlit
* Pickle

---

## 🤖 Models Evaluated
* Logistic Regression
* KNN
* Decision Tree
* Random Forest
* XGBoost

---

## 🏆 Result Summary
XGBoost was selected as the final model after evaluating multiple machine learning algorithms and performing hyperparameter tuning.

### 📈 Final Model Performance
* Accuracy: 96%
* Precision: 97%
* Recall: 95%
* F1-Score: 96%
* ROC-AUC: 99%

### 💡 Why XGBoost?
* Handles complex non-linear relationships effectively through its advanced tree-boosting architecture.
* Prevents overfitting and improves generalization on unseen passenger data using built-in L1 and L2 regularization.
* Delivers balanced Precision and Recall by optimizing custom loss functions and handling class imbalances efficiently.
* Offers exceptional training speed and scalability compared to traditional Gradient Boosting, utilizing parallel processing, tree pruning, and hardware optimization.

---

## 🚀 Business Impact
The model enables airlines to proactively identify dissatisfied passengers, improve service quality, reduce customer churn, and make data-driven decisions to enhance the overall travel experience.
