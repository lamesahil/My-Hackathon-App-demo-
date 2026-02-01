import streamlit as st
# 1. Bada Heading
st.title("Hackathon Registration 🚀")
# 2. Input Fields
name = st.text_input("Enter your name:")
email = st.text_input("Enter your email:")
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)
branch = st.selectbox("Select your branch:", ["Computer Science", "Mechanical", "Electrical", "Civil", "Other"])

# 3. Submit Button
if st.button("Register"):
    st.success(f"Success! {name}, aged {age}, from {branch} branch, you have been registered for the Hackathon.")