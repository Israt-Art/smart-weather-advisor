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
├── 📁 ml_notebook/ ← Colab notebook & data
│ ├── Ai_Weather.ipynb ← Main notebook (80 cells)
│ ├── DailyDelhiClimateTest.csv ← Original raw dataset
│ └── DailyDelhiClimate_Cleaned.csv ← Cleaned & labeled dataset
│
├── 📁 models/ ← All saved ML models
│ ├── model.pkl ← Experiment 1 (Naive Bayes)
│ ├── model_best.pkl ← Experiment 2 (Decision Tree)
│ ├── model_final.pkl ← Experiment 3 (with meantemp)
│ ├── model_new.pkl ← Experiment 4 (balanced NB)
│ ├── model_raw.pkl ← ✅ Final deployed model
│ ├── scaler.pkl ← Scaler v1
│ ├── scaler_final.pkl ← Scaler v2
│ ├── scaler_new.pkl ← Scaler v3
│ └── scaler_raw.pkl ← ✅ Final deployed scaler
│
├── 📁 screenshots admin/ ← Admin view screenshots
│ ├── login_admin.png
│ ├── prediction_cold.png
│ ├── prediction_hot.png
│ ├── prediction_mild.png
│ ├── model_details_top.png
│ ├── model_details_bottom.png
│ ├── user_management.png
│ ├── visualization_top.png
│ ├── visualization_bottom.png
│ └── about.png
│
├── 📁 screenshots user/ ← User view screenshots
│ ├── login_user.png
│ ├── home_user.png
│ ├── visualization_user_top.png
│ ├── visualization_user_bottom.png
│ └── about_user.png
│
└── 📁 web_app/ ← Streamlit web application
├── app.py ← Main app code
├── model_raw.pkl ← ✅ Model used by app
├── requirements.txt ← Python dependencies
└── scaler_raw.pkl ← ✅ Scaler used by app

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

http://localhost:8501


---


---




---

## 🔐 Login Credentials

| Role | Username | Password | Access |
|---|---|---|---|
| 👑 Admin | admin | weather123 | Full access (5 pages) |
| 👤 User | user | delhi123 | Limited access (3 pages) |

---

## 📱 App Pages

| Page | Admin | User |
|---|---|---|
| 🏠 Home & Predict | ✅ | ✅ |
| 📊 Data Visualization | ✅ | ✅ |
| 🔬 Model Details | ✅ | ❌ |
| 👥 User Management | ✅ | ❌ |
| ℹ️ About | ✅ | ✅ |

---

## 📸 App Screenshots

### 👑 Admin View

#### 🔐 Login Page (Admin)
![Login Admin](<screenshots admin/login_admin.png.png>)

---

#### 🔴 Prediction — Hot Weather
![Prediction Hot](<screenshots admin/prediction_hot.png.png>)

---

#### 🟡 Prediction — Mild Weather
![Prediction Mild](<screenshots admin/prediction_mild.png.png>)

---

#### 🔵 Prediction — Cold Weather
![Prediction Cold](<screenshots admin/prediction_cold.png.png>)

---

#### 📊 Data Visualization (Top)
![Visualization Top](<screenshots admin/visualization_top.png.png>)

---

#### 📊 Data Visualization (Bottom)
![Visualization Bottom](<screenshots admin/visualization_bottom.png.png>)

---

#### 🔬 Model Details — Top (Admin Only)
![Model Details Top](<screenshots admin/model_details_top.png.png>)

---

#### 🔬 Model Details — Bottom (Admin Only)
![Model Details Bottom](<screenshots admin/model_details_bottom.png.png>)

---

#### 👥 User Management (Admin Only)
![User Management](<screenshots admin/user_management.png.png>)

---

#### ℹ️ About Page (Admin)
![About Admin](<screenshots admin/about.png.png>)

---

### 👤 User View

#### 🔐 Login Page (User)
![Login User](<screenshots user/login_user.png.png>)

---

#### 🏠 Home & Predict Page (User)
![Home User](<screenshots user/home_user.png.png>)

---

#### 📊 Data Visualization Top (User)
![Visualization User Top](<screenshots user/visualization_user_top.png.png>)

---

#### 📊 Data Visualization Bottom (User)
![Visualization User Bottom](<screenshots user/visualization_user_bottom.png.png>)

---

#### ℹ️ About Page (User)
![About User](<screenshots user/about_user.png.png>)

---

## 📊 Preprocessing Steps

1. ✅ Loaded & explored raw dataset
2. ✅ Checked missing values → None found
3. ✅ Checked duplicates → None found
4. ✅ Fixed outlier in meanpressure (59.0 → 1012.74)
5. ✅ Parsed date → extracted month & day
6. ✅ Created season labels (Winter/Spring/Summer/Autumn)
7. ✅ Created temperature labels (Cold/Mild/Hot)
8. ✅ Normalized features using MinMaxScaler

---

## 📈 Visualizations Included

| # | Chart | Type | Library |
|---|---|---|---|
| 1 | Temperature Over Time | Line Chart | Matplotlib |
| 2 | Season Distribution | Bar Chart | Matplotlib |
| 3 | Temperature Category | Pie Chart | Matplotlib |
| 4 | Feature Correlation | Heatmap | Seaborn |
| 5 | Model Accuracy Comparison | Bar Chart | Matplotlib |
| 6 | Confusion Matrix (Best Model) | Heatmap | Seaborn |
| 7 | Train vs Val vs Test | Grouped Bar | Matplotlib |
| 8 | Confusion Matrix (All Models) | Heatmap Grid | Seaborn |
| 9 | Test Accuracy Comparison | Bar Chart | Matplotlib |
| 10 | All 4 Metrics Comparison | Grouped Bar | Matplotlib |
| 11 | F1 Score Comparison | Bar Chart | Matplotlib |
| 12 | Complete Performance Heatmap | Heatmap | Seaborn |
| 13 | Model Comparison | Radar Chart | Matplotlib |
| 14 | Performance Trend | Line Chart | Matplotlib |

**Total: 14 Visualizations**

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.14 | Programming language |
| Pandas & NumPy | Data manipulation |
| Scikit-learn | ML models |
| Matplotlib & Seaborn | Visualizations |
| Streamlit | Web framework |
| Google Colab | Model training |
| Pickle | Model saving |
| GitHub | Version control |

---

## 👥 Team Members

| Member | Role |
|---|---|
| Member 1 (Israt) | Data Collection & Preprocessing |
| Member 2 (Tasfa) | Model Training, Evaluation & Deployment |

---

## 📅 Course Information

- **Course:** Artificial Intelligence
- **Project:** Weather Classification & Smart Advisory System
- **Dataset:** Daily Delhi Climate (Kaggle)
- **Institution:** United International University
- **Submitted:** June 2026

---

## 🔗 Links

- 📓 **Colab Notebook:** [View Notebook](https://github.com/Israt-Art/smart-weather-advisor/blob/main/ml_notebook/Ai_Weather.ipynb)
- 📊 **Dataset:** [Kaggle - Daily Delhi Climate](https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data)
- 🌐 **Live App:** [delhi-climate-advisor.streamlit.app](https://delhi-climate-advisor.streamlit.app)

---

## ⚠️ Key Findings

- Decision Tree has highest test accuracy (88.89%) but overfits
- Naive Bayes is most balanced — no overfitting (recommended)
- SVM completely failed on this small 114 sample dataset
- Cold class has low prediction due to class imbalance (only 13 samples)
- Dataset is too small — more data would improve all models

---

⭐ If you found this project helpful, please give it a star!

---

*Built with ❤️ using Python & Streamlit*
