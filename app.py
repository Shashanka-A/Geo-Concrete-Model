import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("🧱 Geopolymer Concrete Strength Predictor")
st.markdown("Enter mix design parameters to predict 28-day compressive strength (MPa).")

# Input fields
fly_ash = st.number_input("Fly Ash (%)", min_value=0.0, max_value=100.0, value=50.0)
ggbs = st.number_input("GGBS (%)", min_value=0.0, max_value=100.0, value=50.0)
na2o = st.number_input("Na₂O (M)", min_value=0.0, max_value=20.0, value=10.0)
na2sio3_naoh = st.number_input("Na₂SiO₃ / NaOH Ratio", min_value=0.0, max_value=5.0, value=2.5)
alkali_binder = st.number_input("Alkaline Solution / Binder Ratio", min_value=0.0, max_value=1.0, value=0.4)
water_binder = st.number_input("Water / Binder Ratio", min_value=0.0, max_value=2.0, value=0.5)

# Predict
if st.button("Predict"):
    input_df = pd.DataFrame([{
        "Fly_ash_pct": fly_ash,
        "GGBS_pct": ggbs,
        "Na2O_M": na2o,
        "Na2SiO3_NaOH": na2sio3_naoh,
        "Alkali_Binder_Ratio": alkali_binder,
        "Water_Binder": water_binder
    }])
    prediction = model.predict(input_df)[0]
    st.success(f"🧪 Predicted Compressive Strength: **{prediction:.2f} MPa**")
