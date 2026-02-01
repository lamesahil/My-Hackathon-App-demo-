import streamlit as st
import pandas as pd
import numpy as np

# 1. SIDEBAR CONFIGURATION (Menu)
st.sidebar.title("📱 QuadCore App")
page = st.sidebar.radio("Go to:", ["Home", "Stock Dashboard", "Registration"])

# 2. PAGE 1: HOME
if page == "Home":
    st.title("🏠 Welcome to Team QuadCore")
    st.image("https://media.giphy.com/media/Q81NcsY6YxK7nxfFD0/giphy.gif", width=300) # Fun GIF
    st.write("""
    Ye humara **All-in-One Solution** hai.
    👈 Side menu se alag-alag pages check karein.
    """)
    st.info("Hackathon ke liye hum ready hain! 🦁")

# 3. PAGE 2: STOCK DASHBOARD (Tera Graph wala code)
elif page == "Stock Dashboard":
    st.title("📈 Market Analysis")
    
    # Wahi purana logic
    data = pd.DataFrame(np.random.randn(50, 3), columns=['Railways', 'ITBEES', 'Gold'])
    st.line_chart(data)
    
    if st.checkbox("Show Raw Data"):
        st.write(data) # Table bhi dikha sakte hain!

# 4. PAGE 3: REGISTRATION (Tera Form wala code)
elif page == "Registration":
    st.title("📝 Join the Team")
    
    name = st.text_input("Naam:")
    role = st.selectbox("Role:", ["Coder", "Designer", "Presenter"])
    
    if st.button("Submit"):
        st.success(f"Welcome {name}! You are the new {role}.")