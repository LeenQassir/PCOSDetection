import streamlit as st
from PIL import Image
import base64

# --- Page Config ---
st.set_page_config(page_title="PCOS Detection | AI Diagnostic", layout="centered", page_icon="🩺")

# --- Custom CSS for Cleaner Look ---
st.markdown("""
    <style>
    .main {background-color: #f8f9fa;}
    h1, h2, h3 {color: #2c3e50;}
    .stButton button {background-color: #4CAF50; color: white; font-size: 16px; padding: 10px 24px; border-radius: 8px;}
    .stButton button:hover {background-color: #45a049;}
    </style>
""", unsafe_allow_html=True)

# --- Title and Description ---
st.title("🩺 PCOS Detection using AI")
st.markdown("""
Welcome to the **AI-Powered PCOS Detection Platform**.  
Upload an ultrasound image to perform an initial AI-based screening for Polycystic Ovary Syndrome (PCOS).  
*Note: This tool is for preliminary analysis and does not replace professional medical advice.*
""")

# --- Upload Section ---
st.markdown("---")
uploaded_file = st.file_uploader("📤 Upload an Ultrasound Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="📸 Uploaded Image", use_column_width=True)

    st.markdown("---")
    if st.button("🔍 Analyze Image"):
        st.subheader("📊 AI Diagnostic Result")
        st.success("✅ No indicators of PCOS detected. (Simulated result)")
        st.info("*Note: AI model integration is pending. This is a demonstration interface.*")

# --- Footer ---
st.markdown("---")
st.caption("© 2025 PCOS Detection AI | For Medical Research Use Only.")

