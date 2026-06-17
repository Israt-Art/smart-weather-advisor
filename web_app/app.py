import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ─── Page Config ───────────────────────────────
st.set_page_config(
    page_title="Delhi Climate Advisor",
    page_icon="🌤️",
    layout="wide"
)

# ─── Load Model & Scaler ───────────────────────
@st.cache_resource
def load_model():
    with open('model_raw.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler_raw.pkl', 'rb') as f:
        scaler = pickle.load(f)
    return model, scaler

model, scaler = load_model()

# ─── Login System ──────────────────────────────
def login():
    st.title("🌤️ Delhi Climate Advisor")
    st.subheader("Please login to continue")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        username = st.text_input("👤 Username")
        password = st.text_input("🔒 Password", type="password")

        if st.button("Login", use_container_width=True):
            if username == "admin" and password == "weather123":
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.session_state['role'] = 'admin'
                st.rerun()
            elif username == "user" and password == "delhi123":
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.session_state['role'] = 'user'
                st.rerun()
            else:
                st.error("❌ Wrong username or password!")

        st.info("""
        **Demo Accounts:**
        - 👑 Admin → Username: `admin` | Password: `weather123`
        - 👤 User  → Username: `user`  | Password: `delhi123`
        """)

# ─── Suggestions ───────────────────────────────
def get_suggestions(label):
    suggestions = {
        'Hot': {
            'clothing': [
                "👕 Wear light cotton clothes",
                "🧢 Use a hat or cap outdoors",
                "🕶️ Carry sunglasses",
                "👟 Wear breathable footwear"
            ],
            'activities': [
                "🏊 Swimming is perfect today",
                "🌅 Go out early morning or evening only",
                "❄️ Indoor activities recommended",
                "🚴 Avoid cycling between 11am - 4pm"
            ],
            'health': [
                "💧 Drink at least 3 liters of water",
                "🧴 Apply sunscreen SPF 50+",
                "🥗 Eat light meals — avoid heavy food",
                "⚠️ Risk of heatstroke — stay cool"
            ]
        },
        'Mild': {
            'clothing': [
                "👔 Comfortable casuals work perfectly",
                "🧥 Light jacket for evenings",
                "👟 Any footwear is fine",
                "🎽 Perfect weather for all clothes"
            ],
            'activities': [
                "🏃 Great day for morning jog!",
                "🌳 Perfect for park walks",
                "🚴 Cycling weather is ideal",
                "⛺ Outdoor picnic recommended"
            ],
            'health': [
                "😊 Enjoy the pleasant weather!",
                "🥗 Normal balanced diet",
                "💧 Drink 2 liters of water",
                "🧘 Great day for outdoor yoga"
            ]
        },
        'Cold': {
            'clothing': [
                "🧥 Wear warm layers",
                "🧣 Don't forget scarf and gloves",
                "🥾 Wear warm boots",
                "🧤 Keep hands warm"
            ],
            'activities': [
                "☕ Perfect for indoor activities",
                "🏃 Morning walk with warm clothes",
                "🎯 Indoor sports recommended",
                "🌄 Beautiful cold weather photography!"
            ],
            'health': [
                "🤧 Watch out for flu and cold",
                "☕ Drink warm fluids",
                "💊 Take Vitamin C",
                "🏠 Keep yourself warm indoors"
            ]
        }
    }
    return suggestions[label]

# ─── Admin Sidebar ─────────────────────────────
def admin_panel():
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 👑 Admin Panel")
    st.sidebar.success("Logged in as Admin")
    st.sidebar.markdown("""
    **System Info:**
    - 🤖 Model: Decision Tree
    - 📊 Dataset: 114 samples
    - 🎯 Test Accuracy: 100%
    - 📅 Last Updated: June 2026
    """)
    st.sidebar.markdown("""
    **Registered Users:**
    - 👑 admin (Administrator)
    - 👤 user (Regular User)
    """)
    st.sidebar.markdown("""
    **Model Performance:**
    - ✅ Decision Tree: 88.89%
    - 🌳 Random Forest: 83.33%
    - 📊 Naive Bayes: 77.78%
    - 📍 KNN: 72.22%
    - ❌ SVM: 50.00%
    """)

# ─── Main App ──────────────────────────────────
def main_app():
    role = st.session_state['role']
    username = st.session_state['username']

    # Header
    st.title("🌤️ Delhi Climate Advisor")
    if role == 'admin':
        st.markdown(f"Welcome, **{username}** 👑 `Administrator`")
    else:
        st.markdown(f"Welcome, **{username}** 👤 `User`")

    # Logout
    col1, col2 = st.columns([6, 1])
    with col2:
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.session_state['role'] = None
            st.rerun()

    st.markdown("---")

    # ── Sidebar Navigation ──
    if role == 'admin':
        page = st.sidebar.selectbox(
            "📌 Navigation",
            [
                "🏠 Home & Predict",
                "📊 Data Visualization",
                "🔬 Model Details",
                "👥 User Management",
                "ℹ️ About"
            ]
        )
        admin_panel()
    else:
        page = st.sidebar.selectbox(
            "📌 Navigation",
            [
                "🏠 Home & Predict",
                "📊 Data Visualization",
                "ℹ️ About"
            ]
        )
        st.sidebar.markdown("---")
        st.sidebar.info("👤 Regular User Account")
        st.sidebar.markdown("""
        **Your Access:**
        - ✅ Weather Prediction
        - ✅ Visualizations
        - ❌ Model Details (Admin only)
        - ❌ User Management (Admin only)
        """)

    # ── Page 1: Home & Predict ──
    if page == "🏠 Home & Predict":
        st.header("🌡️ Weather Condition Predictor")
        st.write("Enter today's weather details to get personalized suggestions!")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📥 Input Weather Data")

            temperature = st.slider(
                "🌡️ Mean Temperature (°C)",
                min_value=0.0, max_value=50.0,
                value=22.0, step=0.5
            )
            humidity = st.slider(
                "💧 Humidity (%)",
                min_value=0.0, max_value=100.0,
                value=60.0, step=0.5
            )
            wind_speed = st.slider(
                "💨 Wind Speed (km/h)",
                min_value=0.0, max_value=30.0,
                value=5.0, step=0.5
            )
            pressure = st.slider(
                "🌀 Mean Pressure (hPa)",
                min_value=990.0, max_value=1030.0,
                value=1010.0, step=0.5
            )
            month = st.selectbox(
                "📅 Month",
                options=list(range(1, 13)),
                format_func=lambda x: [
                    'January', 'February', 'March', 'April',
                    'May', 'June', 'July', 'August',
                    'September', 'October', 'November', 'December'
                ][x-1]
            )
            day = st.slider("📆 Day", 1, 31, 15)

            # Input summary
            st.markdown("---")
            st.markdown("**📋 Your Input Summary:**")
            st.write(f"🌡️ Temperature: {temperature}°C")
            st.write(f"💧 Humidity: {humidity}%")
            st.write(f"💨 Wind Speed: {wind_speed} km/h")
            st.write(f"🌀 Pressure: {pressure} hPa")
            st.write(f"📅 Month: {month} | 📆 Day: {day}")

        with col2:
            st.subheader("🔮 Prediction Result")

            if st.button("🚀 Predict Weather!", 
                         use_container_width=True):
                try:
                    # Create input dataframe
                    input_df = pd.DataFrame([[
                        temperature,
                        humidity,
                        wind_speed,
                        pressure,
                        month,
                        day
                    ]], columns=[
                        'meantemp', 'humidity',
                        'wind_speed', 'meanpressure',
                        'month', 'day'
                    ])

                    # Scale and predict
                    input_scaled = scaler.transform(input_df)
                    prediction = model.predict(input_scaled)[0]

                    # Colored result box
                    color_map = {
                        'Hot': '🔴',
                        'Mild': '🟡',
                        'Cold': '🔵'
                    }
                    bg_color = {
                        'Hot': '#ff4444',
                        'Mild': '#ffaa00',
                        'Cold': '#4444ff'
                    }

                    st.markdown(f"""
                    <div style='background-color:{bg_color[prediction]};
                                padding:20px; border-radius:10px;
                                text-align:center; margin:10px 0;'>
                        <h2 style='color:white; margin:0;'>
                            {color_map[prediction]} Weather: {prediction}
                        </h2>
                    </div>
                    """, unsafe_allow_html=True)

                    # Temperature guide
                    st.markdown("""
                    > 🔵 **Cold** = below 15°C | 
                    🟡 **Mild** = 15°C–25°C | 
                    🔴 **Hot** = above 25°C
                    """)

                    st.markdown("---")

                    # Suggestions
                    suggestions = get_suggestions(prediction)

                    st.subheader("👗 Clothing Suggestions")
                    for item in suggestions['clothing']:
                        st.write(item)

                    st.subheader("🏃 Activity Suggestions")
                    for item in suggestions['activities']:
                        st.write(item)

                    st.subheader("💊 Health Tips")
                    for item in suggestions['health']:
                        st.write(item)

                except Exception as e:
                    st.error(f"Prediction error: {e}")

    # ── Page 2: Data Visualization ──
    elif page == "📊 Data Visualization":
        st.header("📊 Model Performance Visualization")

        models_list = ['Naive Bayes', 'Decision Tree',
                       'Random Forest', 'KNN', 'SVM']
        test_acc  = [77.78, 88.89, 83.33, 72.22, 50.00]
        f1_scores = [79.75, 88.30, 78.75, 67.41, 33.33]

        col1, col2 = st.columns(2)

        with col1:
            fig1, ax1 = plt.subplots(figsize=(8, 5))
            colors = ['gold' if m == 'Decision Tree'
                      else 'steelblue' for m in models_list]
            ax1.bar(models_list, test_acc, color=colors)
            ax1.set_title('Test Accuracy - All Models')
            ax1.set_ylabel('Accuracy (%)')
            ax1.set_ylim(0, 110)
            for i, v in enumerate(test_acc):
                ax1.text(i, v + 1, f'{v}%',
                         ha='center', fontweight='bold')
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig1)

        with col2:
            fig2, ax2 = plt.subplots(figsize=(8, 5))
            colors2 = ['gold' if f == max(f1_scores)
                       else 'coral' for f in f1_scores]
            ax2.bar(models_list, f1_scores, color=colors2)
            ax2.set_title('F1 Score - All Models')
            ax2.set_ylabel('F1 Score (%)')
            ax2.set_ylim(0, 110)
            for i, v in enumerate(f1_scores):
                ax2.text(i, v + 1, f'{v}%',
                         ha='center', fontweight='bold')
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig2)

        # Heatmap
        st.subheader("📊 Complete Performance Heatmap")
        metrics_data = {
            'Test Acc':  [88.89, 83.33, 77.78, 72.22, 50.00],
            'Precision': [90.91, 76.39, 86.19, 71.03, 25.00],
            'Recall':    [88.89, 83.33, 77.78, 72.22, 50.00],
            'F1 Score':  [88.30, 78.75, 79.75, 67.41, 33.33]
        }
        heatmap_df = pd.DataFrame(
            metrics_data, index=models_list
        )
        fig3, ax3 = plt.subplots(figsize=(10, 4))
        sns.heatmap(heatmap_df, annot=True, fmt='.1f',
                    cmap='RdYlGn', ax=ax3,
                    vmin=40, vmax=100)
        ax3.set_title('Performance Heatmap - All Models')
        plt.tight_layout()
        st.pyplot(fig3)

        # Radar chart
        st.subheader("🕸️ Radar Chart")
        categories = ['Test Acc', 'Precision', 
                      'Recall', 'F1 Score']
        N = len(categories)
        angles = [n / float(N) * 2 * np.pi for n in range(N)]
        angles += angles[:1]

        values_dict = {
            'Decision Tree': [88.89, 90.91, 88.89, 88.30],
            'Random Forest': [83.33, 76.39, 83.33, 78.75],
            'Naive Bayes':   [77.78, 86.19, 77.78, 79.75],
            'KNN':           [72.22, 71.03, 72.22, 67.41],
            'SVM':           [50.00, 25.00, 50.00, 33.33]
        }

        fig4, ax4 = plt.subplots(
            figsize=(8, 8),
            subplot_kw=dict(polar=True)
        )
        colors_r = ['blue', 'orange', 'green', 'red', 'purple']

        for i, (name, vals) in enumerate(values_dict.items()):
            vals_plot = vals + vals[:1]
            ax4.plot(angles, vals_plot, 'o-',
                     linewidth=2, label=name,
                     color=colors_r[i])
            ax4.fill(angles, vals_plot,
                     alpha=0.1, color=colors_r[i])

        ax4.set_xticks(angles[:-1])
        ax4.set_xticklabels(categories, fontsize=12)
        ax4.set_ylim(0, 100)
        ax4.set_title('Model Comparison Radar Chart',
                      fontsize=14, pad=20)
        ax4.legend(loc='upper right',
                   bbox_to_anchor=(1.3, 1.1))
        plt.tight_layout()
        st.pyplot(fig4)

    # ── Page 3: Model Details (ADMIN ONLY) ──
    elif page == "🔬 Model Details":
        st.header("🔬 Model Details — Admin Only 👑")

        st.subheader("📊 Full Performance Table")
        data = {
            'Model': ['Decision Tree', 'Random Forest',
                      'Naive Bayes', 'KNN', 'SVM'],
            'Train Acc (%)': [100.0, 100.0, 
                               79.75, 83.54, 63.29],
            'Val Acc (%)':   [64.71, 64.71, 
                               76.47, 64.71, 47.06],
            'Test Acc (%)':  [88.89, 83.33, 
                               77.78, 72.22, 50.00],
            'F1 Score (%)':  [88.30, 78.75, 
                               79.75, 67.41, 33.33],
            'Overfit':       ['⚠️ Yes', '⚠️ Yes',
                              '✅ No', '⚠️ Yes', '⚠️ Yes']
        }
        st.dataframe(
            pd.DataFrame(data),
            use_container_width=True
        )

        st.subheader("🧠 Model Explanations")
        st.markdown("""
        | Model | How it works | Overfit? |
        |---|---|---|
        | Naive Bayes | Probability based | ✅ No |
        | Decision Tree | Flowchart decisions | ⚠️ Yes |
        | Random Forest | 100 trees combined | ⚠️ Yes |
        | KNN | 5 nearest neighbors | ⚠️ Yes |
        | SVM | Best boundary line | ⚠️ Yes |
        """)

        st.subheader("✅ Deployed Model: Decision Tree")
        st.info("""
        **Why Decision Tree for deployment?**
        - Highest test accuracy 88.89%
        - Correctly predicts all 3 classes
        - Fast prediction speed
        - Easy to interpret
        """)

        # Chart
        st.subheader("📊 Train vs Val vs Test")
        models_names = ['Naive Bayes', 'Decision Tree',
                        'Random Forest', 'KNN', 'SVM']
        train_acc = [79.75, 100.0, 100.0, 83.54, 63.29]
        val_acc   = [76.47, 64.71, 64.71, 64.71, 47.06]
        test_acc  = [77.78, 88.89, 83.33, 72.22, 50.00]

        x = np.arange(len(models_names))
        width = 0.25

        fig5, ax5 = plt.subplots(figsize=(12, 6))
        ax5.bar(x - width, train_acc, width,
                label='Train', color='steelblue')
        ax5.bar(x, val_acc, width,
                label='Validation', color='orange')
        ax5.bar(x + width, test_acc, width,
                label='Test', color='green')
        ax5.set_xticks(x)
        ax5.set_xticklabels(models_names)
        ax5.set_title('Train vs Val vs Test — All Models')
        ax5.set_ylabel('Accuracy (%)')
        ax5.set_ylim(0, 120)
        ax5.legend()
        plt.tight_layout()
        st.pyplot(fig5)

    # ── Page 4: User Management (ADMIN ONLY) ──
    elif page == "👥 User Management":
        st.header("👥 User Management — Admin Only 👑")

        st.subheader("Registered Users")
        users_data = {
            'Username':     ['admin', 'user'],
            'Role':         ['👑 Administrator', 
                             '👤 Regular User'],
            'Access Level': ['Full Access', 
                             'Limited Access'],
            'Pages':        ['All 5 pages', 
                             '3 pages only']
        }
        st.dataframe(
            pd.DataFrame(users_data),
            use_container_width=True
        )

        col1, col2 = st.columns(2)
        with col1:
            st.success("""
            **👑 Admin Access:**
            - ✅ Home & Predict
            - ✅ Data Visualization
            - ✅ Model Details
            - ✅ User Management
            - ✅ About
            """)
        with col2:
            st.warning("""
            **👤 User Access:**
            - ✅ Home & Predict
            - ✅ Data Visualization
            - ❌ Model Details
            - ❌ User Management
            - ✅ About
            """)

    # ── Page 5: About ──
    elif page == "ℹ️ About":
        st.header("ℹ️ About This App")
        st.markdown("""
        ### 🌤️ Delhi Climate Advisor

        This app uses **Machine Learning** to predict Delhi
        weather conditions and provide smart daily suggestions.

        **Dataset:** Daily Delhi Climate Dataset (Kaggle)

        **Temperature Categories:**
        - 🔵 Cold  → below 15°C
        - 🟡 Mild  → 15°C to 25°C
        - 🔴 Hot   → above 25°C

        **Models Trained:**
        - ✅ Decision Tree (Deployed — 88.89%)
        - Random Forest (83.33%)
        - Naive Bayes (77.78%)
        - KNN (72.22%)
        - SVM (50.00%)

        **App Features:**
        - 🌡️ Weather condition prediction
        - 👗 Clothing suggestions
        - 🏃 Activity recommendations
        - 💊 Health tips
        - 📊 Model performance visualizations
        - 🔐 Login with role-based access

        **Built with:** Python, Scikit-learn, Streamlit

        **Project:** AI Course — June 2026
        """)

# ─── Entry Point ───────────────────────────────
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'role' not in st.session_state:
    st.session_state['role'] = None

if st.session_state['logged_in']:
    main_app()
else:
    login()