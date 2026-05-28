import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Hospital AI System",
    page_icon="🏥",
    layout="wide"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }

    h1, h2, h3 {
        color: #00FFAA;
    }

    </style>
""", unsafe_allow_html=True)

# Title
st.title("🏥 Hospital AI Queue System")

st.write("AI-powered patient risk prioritization system")

# Sidebar
st.sidebar.header("Patient Information")

# Inputs
name = st.text_input("Patient Name")

age = st.number_input("Age", min_value=0, max_value=120)

heart_rate = st.number_input("Heart Rate (BPM)", min_value=30, max_value=200)

oxygen = st.number_input("Oxygen Level (%)", min_value=50, max_value=100)

temperature = st.number_input("Body Temperature (°C)", min_value=30.0, max_value=45.0)

symptoms = st.text_area("Symptoms")

# Button
if st.button("Analyze Patient"):

    risk = "Stable"
    priority = "Low"

    # AI Risk Logic
    if oxygen < 90 or heart_rate > 130 or temperature > 39:
        risk = "Critical"
        priority = "High"

    elif oxygen < 95 or heart_rate > 100 or temperature > 37.5:
        risk = "Moderate"
        priority = "Medium"

    # Success Message
    st.success("Patient data submitted successfully!")

    # Patient Summary
    st.write("## Patient Summary")

    st.write("👤 Name:", name)
    st.write("🎂 Age:", age)
    st.write("❤️ Heart Rate:", heart_rate)
    st.write("🫁 Oxygen:", oxygen)
    st.write("🌡️ Temperature:", temperature)
    st.write("📝 Symptoms:", symptoms)

    # Risk Results
    st.write("## AI Risk Assessment")

    if risk == "Critical":
        st.error(f"🔴 Risk Level: {risk}")
        st.error("🚨 Immediate medical attention required!")

    elif risk == "Moderate":
        st.warning(f"🟠 Risk Level: {risk}")
        st.warning("⚠️ Patient should be monitored carefully.")

    else:
        st.success(f"🟢 Risk Level: {risk}")
        st.success("✅ Patient condition appears stable.")

    st.write("### Priority Level:", priority)
        # AI Recommendation System

    st.write("## AI Recommendation")

    if risk == "Critical":
        st.error("🚑 Send patient to Emergency Ward immediately.")

    elif risk == "Moderate":
        st.warning("🩺 Recommend doctor consultation and monitoring.")

    else:
        st.success("🏠 Patient can continue normal observation.")
    # Health Metrics Chart

    st.write("## Patient Health Metrics")

    health_data = pd.DataFrame({
        "Metric": ["Heart Rate", "Oxygen Level", "Temperature"],
        "Value": [heart_rate, oxygen, temperature]
    })

    fig = px.bar(
        health_data,
        x="Metric",
        y="Value",
        title="Patient Vital Signs"
    )

    st.plotly_chart(fig)
        # Queue Prioritization System

    st.write("## Hospital Queue Priority")

    if risk == "Critical":
        queue_position = 1

    elif risk == "Moderate":
        queue_position = 2

    else:
        queue_position = 3

    st.write(f"🏥 Queue Position: {queue_position}")

    if queue_position == 1:
        st.error("🚨 PRIORITY PATIENT - Immediate attention required!")

    elif queue_position == 2:
        st.warning("⚠️ Medium priority patient.")

    else:
        st.success("✅ Low priority patient.")
    # AI Doctor Assistant

    st.write("## 🤖 AI Doctor Assistant")

    if risk == "Critical":

        st.error("""
        The patient appears to be in critical condition due to:
        - Low oxygen level
        - High temperature
        - Elevated heart rate

        Immediate emergency care is recommended.
        Possible respiratory or cardiac emergency suspected.
        """)

    elif risk == "Moderate":

        st.warning("""
        Patient shows moderate health risk indicators.
        Monitoring and medical consultation are recommended.
        Symptoms may worsen without treatment.
        """)

    else:

        st.success("""
        Patient vitals appear stable.
        No immediate emergency detected.
        Continue regular observation and hydration.
        """)