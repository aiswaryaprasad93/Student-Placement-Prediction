
import streamlit as st
import pandas as pd
import joblib
model = joblib.load("placement_model.pkl")

st.title("Student Placement Prediction")

ssc = st.number_input("SSC Percentage")
hsc = st.number_input("HSC Percentage")
degree = st.number_input("Degree Percentage")
mba = st.number_input("MBA Percentage")

if st.button("Predict"):
       student = pd.DataFrame([[
    1,
    ssc,
    0,
    hsc,
    0,
    2,
    degree,
    2,
    1,
    85,
    1,
    mba
]], columns=[
    'gender',
    'ssc_p',
    'ssc_b',
    'hsc_p',
    'hsc_b',
    'hsc_s',
    'degree_p',
    'degree_t',
    'workex',
    'etest_p',
    'specialisation',
    'mba_p'
])
       prediction = model.predict(student)[0]

       if prediction == 1:
              st.success("🎉 Prediction: Placed")
       else:
              st.error("❌ Prediction: Not Placed")

      
      
