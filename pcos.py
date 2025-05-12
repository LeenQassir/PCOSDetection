import streamlit as st
from PIL import Image
import numpy as np
import sqlite3
from datetime import datetime
from tensorflow.keras.models import load_model

# --- Page Configuration ---
st.set_page_config(page_title="PCOS Detection | AI Diagnostic", layout="centered", page_icon="🩺")

# --- Load the Trained Model ---
@st.cache_resource
def load_trained_model():
    return load_model("best_mobilenet_model.h5")

model = load_trained_model()

# --- Database Functions ---
def init_db():
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                        patient_id TEXT PRIMARY KEY,
                        name TEXT,
                        age INTEGER,
                        last_prediction TEXT,
                        confidence REAL,
                        last_update TEXT
                    )''')
    conn.commit()
    conn.close()

def get_patient_record(patient_id):
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
    record = cursor.fetchone()
    conn.close()
    return record

def update_patient_record(patient_id, name, age, prediction, confidence):
    conn = sqlite3.connect('patients.db')
    cursor = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''INSERT OR REPLACE INTO patients 
                      (patient_id, name, age, last_prediction, confidence, last_update) 
                      VALUES (?, ?, ?, ?, ?, ?)''', 
                   (patient_id, name, age, prediction, confidence, now))
    conn.commit()
    conn.close()

# Initialize Database
init_db()

# --- Preprocess Uploaded Image ---
def preprocess_image(image_file):
    img = image_file.resize((224, 224))  
    img_array = np.array(img) / 255.0    
    img_array = np.expand_dims(img_array, axis=0)  
    return img_array

# --- UI Layout ---
st.title("PCOS Detection using Artificial Intelligence and Machine Learning")
st.markdown("""
<div style='text-align: center;'>
Welcome to the <strong>AI-Powered PCOS Detection Platform</strong>.<br>
Upload an ultrasound image to perform an initial AI-based screening for Polycystic Ovary Syndrome (PCOS).<br>
<em>Note: This tool is for preliminary analysis and does not replace professional medical advice.</em>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    patient_id = st.text_input("Enter Patient ID (Unique)", placeholder="e.g., P12345")
    patient_name = st.text_input("Enter Patient Name", placeholder="e.g., Jane Doe")
with col2:
    patient_age = st.number_input("Enter Patient Age", min_value=1, max_value=100, step=1)

uploaded_file = st.file_uploader("Upload an Ultrasound Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None and patient_id.strip() != "":
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Ultrasound Image", use_container_width=True)

    st.markdown("---")
    if st.button("Analyze Image"):
        st.subheader("AI Diagnostic Result")

        # Preprocess and Predict
        processed_img = preprocess_image(img)
        prediction = model.predict(processed_img)
        result = "PCOS Detected" if prediction[0][0] > 0.5 else "No PCOS Detected"
        confidence = prediction[0][0] * 100

        # Fetch Previous Record
        prev_record = get_patient_record(patient_id)

        # Update Database
        update_patient_record(patient_id, patient_name, patient_age, result, confidence)

        # Display Results
        st.success(f"**{result}** for **{patient_name.strip() or 'Patient'}**, Age: **{int(patient_age)}**.")
        st.info(f"*Model Confidence: {confidence:.2f}%*")

        if prev_record:
            st.markdown("---")
            st.subheader("📊 Previous Diagnostic Result Found:")
            st.write(f"**Last Diagnosis:** {prev_record[3]}")
            st.write(f"**Confidence:** {prev_record[4]:.2f}%")
            st.write(f"**Last Update:** {prev_record[5]}")
            if prev_record[3] != result:
                st.warning("⚠️ Diagnosis has changed from the last test. Consider medical consultation.")
            else:
                st.success("✅ Diagnosis remains consistent with previous test.")
else:
    if uploaded_file is not None and patient_id.strip() == "":
        st.warning("⚠️ Please provide a unique Patient ID to proceed with the analysis.")

# --- Footer ---
st.markdown("---")
st.markdown("<div style='text-align: center;'>© 2025 PCOS Detection AI | For Medical Research Use Only.</div>", unsafe_allow_html=True)
