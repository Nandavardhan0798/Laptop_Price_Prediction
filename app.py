import streamlit as st
import pandas as pd
import joblib

# Load model and preprocessor
model = joblib.load('model.pkl')
preprocessor = joblib.load('preprocessor.pkl')

st.title("💻 Laptop Price Predictor")

# Collect user input
company = st.selectbox("Company", ['HP', 'Dell', 'Apple', 'Lenovo'])
typename = st.selectbox("Type", ['Notebook', 'Ultrabook', 'Gaming'])
inches = st.number_input("Screen Size (inches)", 10.0, 18.0)
screen = st.text_input("Screen Resolution", '1920x1080')
cpu = st.selectbox("CPU", ['Intel Core i5', 'Intel Core i7', 'AMD Ryzen 5'])
ram = st.selectbox("RAM in GB", [4, 8, 16])
memory = st.selectbox("Storage in GB", [256, 512, 1024])
gpu = st.text_input("GPU", 'Intel HD Graphics 620')
opsys = st.selectbox("Operating System", ['Windows 10', 'MacOS', 'Linux'])
weight = st.selectbox("Weight (kg)", [0.5, 1, 1.5, 2.0])

# Prediction
if st.button("Predict Price"):
    input_data = pd.DataFrame([{
        'Company': company,
        'TypeName': typename,
        'Inches': inches,
        'ScreenResolution': screen,
        'Cpu': cpu,
        'Ram': ram,
        'Memory': memory,
        'Gpu': gpu,
        'OpSys': opsys,
        'Weight': weight
    }])

    transformed = preprocessor.transform(input_data)
    prediction = model.predict(transformed)[0]
    st.success(f"💰 Estimated Laptop Price: ₹{prediction:,.2f}")