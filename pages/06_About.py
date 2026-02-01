import streamlit as st
import pandas as pd
import numpy as np

menu_choice = st.sidebar.selectbox("Select Page", ["BMI Calculator", "Stock Market Dashboard", "Registration Form"])
if menu_choice == "Home":
    st.title("🏠 Welcome to Team QuadCore")
    st.image("https://media.giphy.com/media/Q81NcsY6YxK7nxfFD0/giphy.gif", width=300) # Fun GIF
    st.write("""
    Ye humara **All-in-One Solution** hai.
    👈 In the sidebar menu, you can navigate to different pages.
    """)
    st.info("We are ready for Hackathon 🦁")
elif menu_choice == "BMI Calculator":
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
elif menu_choice == "Stock Market Dashboard":
    st.title("📈 Stock Market Dashboard")
    st.write("This is an interactive graph.")
    data = np.random.randn(50, 3)
    # 1. Fake Data banate hain (Random numbers)
    # Imagine kar ye TCS, Infosys, aur Wipro ke prices hain
    chart_data = pd.DataFrame(
        #np.random.randn(20, 3),
        data,
        columns=['Railways', 'ITBEES', 'Gold']
    )
    # 2. THE MAGIC LINE (Sirf ek line mein pura graph!)
    st.line_chart(chart_data)
    # 3. Bar Chart bhi try kar lete hain
    st.write("Volume Analysis:")
    st.bar_chart(chart_data)
elif menu_choice == "Registration Form":
    st.title("📝 Join the Team")
    
    name = st.text_input("Naam:")
    role = st.selectbox("Role:", ["Coder", "Designer", "Presenter"])
    
    if st.button("Submit"):
        st.success(f"Welcome {name}! You are the new {role}.")  
        