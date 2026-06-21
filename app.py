
import streamlit as st

st.title("Student Placement Prediction")

ssc = st.number_input("SSC Percentage")
hsc = st.number_input("HSC Percentage")
degree = st.number_input("Degree Percentage")
mba = st.number_input("MBA Percentage")

if st.button("Predict"):
    if ssc >= 60 and hsc >= 60 and degree >= 60 and mba >= 60:
        st.success("Prediction: Placed")
    else:
        st.error("Prediction: Not Placed")
