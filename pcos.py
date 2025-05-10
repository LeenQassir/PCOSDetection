import streamlit as st
from PIL import Image

# --- Page Config ---
st.set_page_config(page_title="PCOS Detection | AI Diagnostic", layout="centered", page_icon="🩺")

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
    .main {background-color: #f0f2f6;}
    h1, h2, h3 {color: #2c3e50;}
    .stButton button {background-color: #4CAF50; color: white; font-size: 16px; padding: 10px 24px; border-radius: 8px;}
    .stButton button:hover {background-color: #45a049;}
    .stTextInput>div>div>input {border-radius: 8px;}
    </style>
""", unsafe_allow_html=True)

# --- Title and Description ---
st.title("🩺 PCOS Detection using AI")
st.markdown("""
Welcome to the **AI-Powered PCOS Detection Platform**.  
Upload an ultrasound image to perform an initial AI-based screening for Polycystic Ovary Syndrome (PCOS).  
*Note: This tool is for preliminary analysis and does not replace professional medical advice.*
""")

# --- Patient Name Input ---
patient_name = st.text_input("👤 Enter Patient Name", placeholder="e.g., Jane Doe")

# --- Upload Section ---
st.markdown("---")
uploaded_file = st.file_uploader("📤 Upload an Ultrasound Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="📸 Uploaded Image", use_column_width=True)

    st.markdown("---")
    if st.button("🔍 Analyze Image"):
        st.subheader("📊 AI Diagnostic Result")

        if patient_name.strip() == "":
            patient_name_display = "Patient"
        else:
            patient_name_display = patient_name

        st.success(f"✅ No indicators of PCOS detected for **{patient_name_display}**. (Simulated result)")
        st.info("*Note: AI model integration is pending. This is a demonstration interface.*")

# --- Footer ---
st.markdown("---")
st.caption("© 2025 PCOS Detection AI | For Medical Research Use Only.")


