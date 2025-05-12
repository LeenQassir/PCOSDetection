import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

# --- Page Configuration ---
st.set_page_config(page_title="PCOS Detection | AI Diagnostic", layout="centered", page_icon="🩺")

# --- Load the Trained Model ---
@st.cache_resource
def load_trained_model():
    return load_model("best_mobilenet_model.h5")

model = load_trained_model()

# --- Preprocess Uploaded Image ---
def preprocess_image(image_file):
    img = image_file.resize((224, 224))  # Resize to match model input
    img_array = np.array(img) / 255.0    # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# --- Custom CSS Styling ---
st.markdown("""
    <style>
    body, .stApp {
        background-color: #f0f2f6;
    }
    h1, h2, h3 {
        color: #2c3e50;
        text-align: center;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        border-radius: 8px;
    }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- Title and Description ---
st.title("PCOS Detection using Artificial Intelligence and Machine Learning")
st.markdown("""
<div style='text-align: center;'>
Welcome to the <strong>AI-Powered PCOS Detection Platform</strong>.<br>
Upload an ultrasound image to perform an initial AI-based screening for Polycystic Ovary Syndrome (PCOS).<br>
<em>Note: This tool is for preliminary analysis and does not replace professional medical advice.</em>
</div>
""", unsafe_allow_html=True)

# --- Patient Information ---
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    patient_name = st.text_input("Enter Patient Name", placeholder="e.g., Jane Doe")
with col2:
    patient_age = st.number_input("Enter Patient Age", min_value=1, max_value=100, step=1)

# --- Upload Image ---
uploaded_file = st.file_uploader("Upload an Ultrasound Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Ultrasound Image", use_container_width=True)

    st.markdown("---")
    if st.button("Analyze Image"):
        st.subheader("AI Diagnostic Result")

        # Handle empty name
        patient_name_display = patient_name.strip() if patient_name.strip() else "Patient"

        # Preprocess and Predict
        processed_img = preprocess_image(img)
        prediction = model.predict(processed_img)
        result = "PCOS Detected" if prediction[0][0] > 0.5 else "No PCOS Detected"
        confidence = prediction[0][0] * 100

        # Display Result
        st.success(f"**{result}** for **{patient_name_display}**, Age: **{int(patient_age)}**.")
        st.info(f"*Model Confidence: {confidence:.2f}%*")

# --- Footer ---
st.markdown("---")
st.markdown("<div style='text-align: center;'>© 2025 PCOS Detection AI | For Medical Research Use Only.</div>", unsafe_allow_html=True)
