import streamlit as st
import pandas as pd
import numpy as np

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