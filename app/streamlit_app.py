import streamlit as st
import requests

st.set_page_config(layout="wide")
st.title("🌞 Solar Desalination Forecast Dashboard")

st.sidebar.header("Input Features")
inputs = {
    "actual_irr": st.sidebar.slider("Actual Irradiance", 1.0, 30.0, 20.0),
    "clear_sky_irr": st.sidebar.slider("Clear-sky Irradiance", 1.0, 30.0, 25.0),
    "month": st.sidebar.selectbox("Month", list(range(1, 13))),
    "temp": st.sidebar.slider("Temperature (°C)", 10.0, 50.0, 35.0),
    "pressure": st.sidebar.slider("Surface Pressure (kPa)", 95.0, 105.0, 100.0),
    "dew_point": st.sidebar.slider("Dew Point", 1.0, 30.0, 15.0),
    "wind": st.sidebar.slider("Wind Speed (m/s)", 1.0, 10.0, 3.0),
    "humidity": st.sidebar.slider("Humidity (%)", 1.0, 25.0, 10.0),
    "aod_lag1": st.sidebar.slider("Previous Day AOD", 100, 4000, 2000),
    "aod_lag2": st.sidebar.slider("AOD 2 Days Ago", 100, 4000, 1800),
    "aod_roll3": st.sidebar.slider("3-Day Avg AOD", 100, 4000, 1900),
}

if st.button("🔮 Predict"):
    try:
        res = requests.post("http://localhost:8000/predict", json=inputs)
        if res.status_code == 200:
            out = res.json()
            st.success(f"Predicted AOD: {out['predicted_aod']:.2f}")
            st.success(f"Efficiency Loss: {out['efficiency_loss_pct']:.2f}%")
            st.info(f"Severity Level: {out['severity_level']}")
            st.subheader("Control Recommendations")
            st.write(f"🔧 Pressure Control: {out['control_messages']['pressure_control']}")
            st.write(f"🧼 System Maintenance: {out['control_messages']['system_maintenance']}")
            st.write(f"⚡ Energy Source: {out['control_messages']['energy_source']}")
        else:
            st.error(f"Error: {res.status_code} - {res.text}")
    except Exception as e:
        st.error(f"API Error: {e}")