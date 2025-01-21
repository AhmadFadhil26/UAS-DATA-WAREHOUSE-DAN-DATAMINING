# app.py

import streamlit as st
import numpy as np
import pickle

# Load the model
with open('model_uas.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app
st.title("Prediksi Pembayaran Premi Asuransi")
st.write("NIM: 2021230048")  
st.write("Nama: Ahmad Fadhil Firmansyah")  

# Input fields
age = st.number_input('Umur', min_value=0, max_value=100, value=25)
sex = st.selectbox('Jenis Kelamin', options=[('Laki-laki', 1), ('Perempuan', 0)], format_func=lambda x: x[0])
bmi = st.number_input('BMI', min_value=0.0, max_value=50.0, value=25.0)
children = st.number_input('Jumlah Anak', min_value=0, max_value=10, value=0)
smoker = st.selectbox('Perokok', options=[('Ya', 1), ('Tidak', 0)], format_func=lambda x: x[0])

# Convert sex and smoker to numerical values
sex = sex[1]
smoker = smoker[1]

# Predict button
if st.button('Submit'):
    # Prepare input data
    input_data = np.array([age, sex, bmi, children, smoker]).reshape(1, -1)
    
    # Predict
    prediction = model.predict(input_data)
    
    # Display prediction
    st.write(f"Prediksi Pembayaran Premi: {prediction[0]:.2f}")