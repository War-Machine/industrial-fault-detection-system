import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Industrial Fault Detection", layout="wide")

st.title("⚠ Industrial Fault Detection System")

temperature = random.randint(20, 100)
pressure = random.randint(80, 150)
vibration = random.randint(0, 10)

col1, col2, col3 = st.columns(3)

col1.metric("Temperature", f"{temperature} °C")
col2.metric("Pressure", f"{pressure} PSI")
col3.metric("Vibration", vibration)

if temperature > 80:
    st.error("⚠ High Temperature Fault Detected")

if pressure > 130:
    st.warning("⚠ Pressure Limit Exceeded")

if vibration > 7:
    st.error("⚠ Excessive Machine Vibration")

data = pd.DataFrame({
    "Temperature": [random.randint(20,100) for i in range(10)],
    "Pressure": [random.randint(80,150) for i in range(10)],
})

st.line_chart(data)

st.success("Monitoring System Active")
