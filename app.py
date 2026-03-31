import streamlit as st
import pandas as pd
import joblib

model = joblib.load('flight_model.pkl')

st.title("Flight Price Predictor")

airline  = st.selectbox("Airline", ['IndiGo','Air India','Vistara','GO FIRST','AirAsia','SpiceJet'])
source   = st.selectbox("From", ['Delhi','Mumbai','Bangalore','Kolkata','Hyderabad','Chennai'])
dest     = st.selectbox("To", ['Delhi','Mumbai','Bangalore','Kolkata','Hyderabad','Chennai'])
cls      = st.selectbox("Class", ['Economy','Business'])
stops    = st.selectbox("Stops", ['zero','one','two_or_more'])
dep_time = st.selectbox("Departure Time", ['Morning','Afternoon','Evening','Night','Early_Morning','Late_Night'])
arr_time = st.selectbox("Arrival Time", ['Morning','Afternoon','Evening','Night','Early_Morning','Late_Night'])
days     = st.slider("Days before departure", 1, 49, 15)
duration = st.slider("Duration (hours)", 1, 50, 3)

if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        'airline': airline, 'source_city': source,
        'destination_city': dest, 'stops': stops,
        'days_left': days, 'duration': duration,
        'departure_time': dep_time, 'arrival_time': arr_time,
        'class': cls
    }])
    price = model.predict(input_df)[0]
    st.success(f"Estimated Price: Rs.{price:,.0f}")


import os
print(os.getcwd())