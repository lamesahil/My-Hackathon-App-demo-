import streamlit as st

st.title("🦁 Meet Team QuadCore")
st.write("We are a group of passionate engineers from TCET, building the future.")
st.markdown("---")

# --- ROW 1 (Sahil & Anuvesh) ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sahil Tiwari")
    st.caption("🎓 B.E. (IT) - TCET")
    st.write("The Architect & Frontend Lead.")
    # Special Blog Button for You
    st.link_button("🌐 Visit My Blog", "http://www.sahillog.me")
    st.markdown("[📸 Instagram](https://www.instagram.com/lamesahil)")

with col2:
    st.subheader("Anuvesh Tiwari")
    st.caption("🎓 B.E. (IT) - TCET")
    st.write("Tech Enthusiast & Coder.")
    st.markdown("[📸 Instagram](https://www.instagram.com/aanuvesh_24)")

st.markdown("---")

# --- ROW 2 (Kshitij & Omkar) ---
col3, col4 = st.columns(2)

with col3:
    st.subheader("Kshitij Singh")
    st.caption("🎓 B.E. (AIML) - TCET")
    st.write("AI/ML Expert.")
    st.markdown("[📸 Instagram](https://www.instagram.com/known_one4u)")

with col4:
    st.subheader("Omkar Dubey")
    st.caption("🎓 B.E. (IT) - TCET")
    st.write("Backend & Database Support.")
    st.markdown("[📸 Instagram](https://www.instagram.com/dubey_omii_.05)")

st.markdown("---")
st.success("Feel free to connect with us! 🚀")