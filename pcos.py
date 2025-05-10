import streamlit as st
from PIL import Image
import time

# --- Page Configuration ---
st.set_page_config(page_title="PCOS Detection | AI Diagnostic", layout="centered", page_icon="🩺")

# --- Custom CSS ---
st.markdown("""
    <style>
    body, .stApp {background-color: #f0f2f6;}
    h1, h2, h3 {color: #2c3e50; text-align: center;}
    .stButton button {
        background-color: #4CAF50; color: white; font-size: 16px; 
        padding: 10px 24px; border-radius: 8px;
    }
    .stButton button:hover {background-color: #45a049;}
    .stTextInput>div>div>input, .stNumberInput>div>div>input {border-radius: 8px;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Branding ---
with st.sidebar:
    st.image("https://i.imgur.com/llF5iyg.png", width=150)  # Replace with your logo link
    st.markdown("###  PCOS Detection AI")
    st.markdown("**Version:** 1.0.0")
    st.markdown("---")
    st.markdown(" Contact: support@pcos-ai.com")
    st.markdown(" [Visit Website](https://www.pcos-ai.com)")
    st.markdown("---")

# --- Main Title and Description ---
st.title(" PCOS Detection using AI")
st.markdown("""
<div style='text-align: center;'>
Welcome to the <strong>AI-Powered PCOS Detection Platform</strong>.<br>
Upload an ultrasound image to perform an initial AI-based screening for Polycystic Ovary Syndrome (PCOS).<br>
<em>Note: This tool is for preliminary analysis and does not replace professional medical advice.</em>
</div>
""", unsafe_allow_html=True)

# --- Patient Information Card ---
st.markdown("###  Patient Information")
col1, col2 = st.columns(2)

with col1:
    patient_name = st.text_input(" Enter Patient Name", placeholder="e.g., Jane Doe")

with col2:
    patient_age = st.number_input(" Enter Patient Age", min_value=1, max_value=100, step=1)

# --- Upload Section ---
st.markdown("---")
uploaded_file = st.file_uploader(" Upload an Ultrasound Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption=" Uploaded Ultrasound Image", use_column_width=True)

    if st.button("🔍 Start Analysis"):
        # Validate inputs
        if not patient_name.strip():
            st.warning(" Please enter the patient's name before proceeding.")
        else:
            with st.spinner("Analyzing..."):
                # Simulate analysis time
                progress_bar = st.progress(0)
                for percent_complete in range(100):
                    time.sleep(0.02)
                    progress_bar.progress(percent_complete + 1)

            st.subheader("AI Diagnostic Result")
            st.success(f" No indicators of PCOS detected for **{patient_name}**, Age: **{int(patient_age)}**. (Simulated Result)")
            st.info("*Note: AI model integration is pending. This is a demonstration interface.*")

# --- Footer ---
st.markdown("---")
st.markdown("<div style='text-align: center;'>© 2025 PCOS Detection AI | For Medical Research Use Only.</div>", unsafe_allow_html=True)
