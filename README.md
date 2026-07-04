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


smart-weather-advisor/
│
├── 📁 ml_notebook/
│   ├── Ai_Weather.ipynb              # Main Colab notebook
│   ├── DailyDelhiClimateTest.csv     # Original dataset
│   └── DailyDelhiClimate_Cleaned.csv # Cleaned dataset
│
├── 📁 models/
│   ├── model_raw.pkl                 # ✅ Final deployed model
│   ├── scaler_raw.pkl                # ✅ Final scaler
│   ├── model.pkl                     # Experiment 1
│   ├── model_new.pkl                 # Experiment 2
│   ├── model_best.pkl                # Experiment 3
│   ├── model_final.pkl               # Experiment 4
│   ├── scaler.pkl                    # Scaler v1
│   ├── scaler_new.pkl                # Scaler v2
│   └── scaler_final.pkl              # Scaler v3
│
└── 📁 web_app/
├── app.py                        # Main Streamlit app
├── requirements.txt              # Dependencies
├── model_raw.pkl                 # Model for deployment
└── scaler_raw.pkl                # Scaler for deployment
