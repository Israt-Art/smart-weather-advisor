# 🌤️ Delhi Climate Advisor

An AI-powered web application that predicts Delhi weather conditions 
and provides smart personalized suggestions using Machine Learning.

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.58-red)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.9-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Project Overview

This project was developed as part of an AI course project. It uses 
the Daily Delhi Climate Dataset to classify weather conditions into 
**Cold**, **Mild**, or **Hot** categories and provides real-time 
suggestions for clothing, outdoor activities, and health tips.

The project covers the complete Machine Learning pipeline from data 
collection and preprocessing to model training, evaluation, 
comparison and final web app deployment.

---

## 🎯 App Features

- 🔐 **Login System** with Role-based Access (Admin / User)
- 🌡️ **Weather Prediction** (Cold / Mild / Hot)
- 👗 **Clothing Suggestions** based on weather
- 🏃 **Activity Recommendations** for the day
- 💊 **Health Tips** based on weather condition
- 📊 **Model Performance Visualizations**
- 👥 **User Management** (Admin only)
- 🔬 **Model Details Panel** (Admin only)

---

## 📁 Project Structure


```
smart-weather-advisor/
│
├── 📁 ml_notebook/                       ← Colab notebook & data
│   ├── Ai_Weather.ipynb                  ← Main notebook (80 cells)
│   ├── DailyDelhiClimateTest.csv         ← Original raw dataset
│   └── DailyDelhiClimate_Cleaned.csv     ← Cleaned & labeled dataset
│
├── 📁 models/                            ← All saved ML models
│   ├── model.pkl                         ← Experiment 1 (Naive Bayes)
│   ├── model_best.pkl                    ← Experiment 2 (Decision Tree)
│   ├── model_final.pkl                   ← Experiment 3 (with meantemp)
│   ├── model_new.pkl                     ← Experiment 4 (balanced NB)
│   ├── model_raw.pkl                     ← ✅ Final deployed model
│   ├── scaler.pkl                        ← Scaler v1
│   ├── scaler_final.pkl                  ← Scaler v2
│   ├── scaler_new.pkl                    ← Scaler v3
│   └── scaler_raw.pkl                    ← ✅ Final deployed scaler
│
└── 📁 web_app/                           ← Streamlit web application
    ├── app.py                            ← Main app code
    ├── model_raw.pkl                     ← ✅ Model used by app
    ├── requirements.txt                  ← Python dependencies
    └── scaler_raw.pkl                    ← ✅ Scaler used by app
```


---

## 🤖 Models Trained & Compared

| Model | Train Acc | Val Acc | Test Acc | F1 Score | Overfit |
|---|---|---|---|---|---|
| Decision Tree | 100% | 64.71% | 88.89% 🏆 | 88.30% | ⚠️ Yes |
| Random Forest | 100% | 64.71% | 83.33% | 78.75% | ⚠️ Yes |
| Naive Bayes | 79.75% | 76.47% | 77.78% | 79.75% | ✅ No |
| KNN | 83.54% | 64.71% | 72.22% | 67.41% | ⚠️ Yes |
| SVM | 63.29% | 47.06% | 50.00% | 33.33% | ⚠️ Yes |

**Deployed Model:** Decision Tree Classifier (88.89% Test Accuracy)

---

## 📊 Dataset Information

- **Source:** Kaggle — Daily Delhi Climate Dataset
- **Size:** 114 rows × 5 columns
- **Features:** date, meantemp, humidity, wind_speed, meanpressure
- **Target:** temp_label (Cold / Mild / Hot)
- **Date Range:** January 2017 — April 2017

**Temperature Categories:**
- 🔵 Cold → below 15°C (13 samples — 11.4%)
- 🟡 Mild → 15°C to 25°C (67 samples — 58.8%)
- 🔴 Hot → above 25°C (34 samples — 29.8%)

---

## 🔧 Complete Project Pipeline

| Step | Task | Status |
|---|---|---|
| 1 | Data Collection (Kaggle) | ✅ Done |
| 2 | Data Preprocessing & Cleaning | ✅ Done |
| 3 | Annotation (Season & Temp Labels) | ✅ Done |
| 4 | Model Selection (5 classifiers) | ✅ Done |
| 5 | Model Training (70/15/15 split) | ✅ Done |
| 6 | Performance Evaluation | ✅ Done |
| 7 | Performance Comparison | ✅ Done |
| 8 | Visualization (Matplotlib & Seaborn) | ✅ Done |
| 9 | Model Deployment (Streamlit) | ✅ Done |

---

## 🚀 How to Run Locally

**Step 1 — Clone the repository:**
```bash
git clone https://github.com/Israt-Art/smart-weather-advisor.git
```

**Step 2 — Go to web_app folder:**
```bash
cd smart-weather-advisor/web_app
```

**Step 3 — Install dependencies:**
```bash
pip install -r requirements.txt
```

**Step 4 — Run the app:**
```bash
streamlit run app.py
```

**Step 5 — Open browser:**
