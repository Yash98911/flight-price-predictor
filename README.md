# ✈️ Flight Price Predictor

A machine learning web application that predicts Indian flight ticket 
prices in real-time using real EaseMyTrip data.

---

## 🔍 Problem Statement
Flight prices in India change constantly based on airline, route, 
timing, and how far in advance you book. This project builds a 
machine learning model that predicts flight ticket prices accurately 
— helping travelers make smarter booking decisions.

---

## 📊 Dataset
- **Source:** EaseMyTrip (via Kaggle)
- **Rows:** 300,261 flights
- **Features:** 11 (airline, source city, destination, stops, 
  departure time, arrival time, class, duration, days left)
- **Target:** Flight Price (₹)

---

## 🔬 Approach

### 1. Exploratory Data Analysis
- Analyzed price distribution across airlines, routes, and classes
- Found that Business class tickets are 6x more expensive than Economy
- Identified that last-minute bookings (< 7 days) cost significantly more
- Discovered duration and days_left as strongest price drivers

### 2. Preprocessing
- Built full Scikit-learn Pipeline with Column Transformer
- One-Hot Encoding for categorical features
- Standard Scaling for numerical features
- Zero data leakage — pipeline fit only on training data

### 3. Model Comparison

| Model | R2 Score | MAE |
|-------|----------|-----|
| Linear Regression | 91% | ₹4,200 |
| Decision Tree | 94% | ₹3,100 |
| Random Forest | 94% | ₹2,900 |
| **XGBoost** | **96%** | **₹2,300** |

### 4. Hyperparameter Tuning
- Used RandomizedSearchCV with 5-fold cross validation
- Tuned n_estimators, max_depth, learning_rate, subsample
- XGBoost selected as final model — best accuracy, lowest error

---

## 💡 Key Business Insights
- **Book 30+ days early** — prices drop significantly vs last minute
- **IndiGo and SpiceJet** offer cheapest Economy fares on average
- **Non-stop flights** are priced 40% higher than 1-stop flights
- **Evening departures** tend to be more expensive than early morning
- **Duration** is the single strongest predictor of flight price

---

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** Scikit-learn, XGBoost, Pandas, NumPy, Streamlit
- **Deployment:** Streamlit Cloud

---

## 🚀 Live Demo
👉 [Click here to try the app](https://flight-price-predictor-jnhtdzg5xcyb3q98g62eb8.streamlit.app/)

---

## 📁 Project Structure
```
flight-price-predictor/
│
├── app.py                  # Streamlit web application
├── flight_model.pkl        # Trained XGBoost pipeline
├── requirements.txt        # Dependencies
├── flight_price_project.ipynb  # Jupyter notebook — full analysis
└── README.md
```

---

## 📈 Results
Final model — **XGBoost with 96% R2 score** and **₹2,300 MAE**
meaning predictions are within ₹2,300 of actual price on average.

---

## 🙋 Author
**Yash Dhollakhandi**  
Data Science Enthusiast | B.Tech [GGSIPU]
