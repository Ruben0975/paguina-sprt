import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import io  # <-- IMPORTANTE para capturar la salida de .info()

# Leer dataset
car_data = pd.read_csv("vehicles_us.csv")

# Título
st.title("Análisis de Datos de Vehículos")

# Primeras filas
st.subheader("Primeras filas del dataset")
st.write(car_data.head())

st.subheader("Información general del dataset")
buffer = io.StringIO()
car_data.info(buf=buffer)
info_str = buffer.getvalue()
st.text(info_str)

st.subheader("Datos faltantes por columna")
st.write(car_data.isnull().sum())

st.subheader("Estadísticas básicas")
st.write(car_data.describe())

st.subheader("Distribución de precios de vehículos")
fig, ax = plt.subplots()
ax.hist(car_data['price'].dropna(), bins=50, edgecolor='black')
ax.set_title("Distribución de precios de vehículos")
ax.set_xlabel("Precio")
ax.set_ylabel("Frecuencia")
st.pyplot(fig)
