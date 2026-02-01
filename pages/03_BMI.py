import streamlit as st
st.title("Health Monitoring Dashboard (BMI)")
st.write("This application calculates your Body Mass Index (BMI) based on your weight and height.")
# Input fields for weight and height
weight = st.number_input("Enter your weight in kilograms (kg):", min_value=1.0, format="%.2f", step=0.5)
height = st.number_input("Enter your height in meters (m):", min_value=0.1, format="%.2f", step=0.01)
#Button to calculate BMI
if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")
    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"
    st.write(f"You are classified as: {category}")
    