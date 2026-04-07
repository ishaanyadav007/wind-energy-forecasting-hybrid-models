import streamlit as st
import numpy as np
import joblib
import tensorflow as tf


model = tf.keras.models.load_model('ANN.keras')
scaler_X = joblib.load('scaler_x.pkl')
scaler_y = joblib.load('scaler_y.pkl')

st.set_page_config(page_title="Wind Power Predictor", layout="centered")
st.title("⚡ Wind Power Output Predictor")
st.markdown("Enter environmental data below to predict wind power output (in kW).")

#Input
temperature = st.number_input("🌡️ Temperature at 2m (°C)", value=25.0)
humidity = st.number_input("💧 Relative Humidity at 2m (%)", value=60.0)
dewpoint = st.number_input("🌫️ Dew Point at 2m (°C)", value=15.0)
windspeed_10 = st.number_input("💨 Windspeed at 10m (m/s)", value=5.0)
windspeed_100 = st.number_input("🌪️ Windspeed at 100m (m/s)", value=7.0)
winddir_10 = st.number_input("🧭 Wind Direction at 10m (°)", value=180.0)
winddir_100 = st.number_input("🧭 Wind Direction at 100m (°)", value=200.0)
windgusts_10 = st.number_input("⚡ Wind Gusts at 10m (m/s)", value=10.0)
hour = st.slider("🕒 Hour of Day", 0, 23, 12)
day_of_week = st.slider("📅 Day of Week (0=Mon, 6=Sun)", 0, 6, 2)
month = st.slider("📆 Month", 1, 12, 4)


if st.button("🔍 Predict Power Output"):
    input_data = np.array([[temperature, humidity, dewpoint,
                            windspeed_10, windspeed_100, winddir_10,
                            winddir_100, windgusts_10, hour,
                            day_of_week, month]])

    input_scaled = scaler_X.transform(input_data)
    prediction_scaled = model.predict(input_scaled)
    predicted_power = scaler_y.inverse_transform(prediction_scaled)[0][0]

    st.success(f"✅ Predicted Power Output: **{predicted_power:.2f} kW**")
