# Airline Passenger Satisfaction Prediction System 😌

## ✈️ Industry Domain
Aviation & Customer Experience 

---

## 🏢 About the Company
SkyRoute Aviation is a passenger-focused airline company that uses customer experience analytics to improve travel services, understand passenger expectations, and strengthen customer satisfaction. The company collects feedback, service ratings, travel details, and operational information to identify service gaps, support better decisions, and deliver a smoother and more comfortable journey for passengers consistently.

---

## 🤔 Problem Statement
SkyRoute Aviation receives thousands of passenger feedback and service records after every flight, but manually identifying dissatisfied passengers is difficult and time-consuming. Without early identification of dissatisfied customers, the airline may miss opportunities to address service issues, improve passenger experience, and reduce customer churn.

---

## 🎯 Objective
Build a classification model that predicts passenger satisfaction using demographic, travel, service rating, and flight experience attributes. The goal is to identify dissatisfied passengers, improve service quality, support proactive customer engagement, and strengthen overall passenger experience for passengers today.

---

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

## 🛠️ Tech Stack
* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-Learn
* Streamlit
* Pickle

---

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
