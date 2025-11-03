import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("insurance_pickle.pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.title("💰 Insurance Charges Prediction App")
st.markdown("### Predict Medical Insurance Cost Based on Age, BMI, and Smoking Status")

# Input fields
age = st.number_input("Enter Age", min_value=0, max_value=100, value=25)
bmi = st.number_input("Enter BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=22.0, step=0.1)
smoker = st.selectbox("Are you a smoker?", ("No", "Yes"))

# Convert smoker input to binary
smoker_yes = 1 if smoker == "Yes" else 0

# Predict button
if st.button("🔮 Predict Charges"):
    # Prepare input for model
    input_data = np.array([[age, bmi, smoker_yes]])
    prediction = model.predict(input_data)
    
    st.success(f"💵 Estimated Insurance Charges: **${prediction[0]:,.2f}**")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit and Scikit-learn")
