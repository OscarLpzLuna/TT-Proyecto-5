import streamlit as st
import pandas as pd
import plotly_express as px


# Se carga el dataset de interés
data = pd.read_csv('vehicles_us.csv')

st.header('Datos recabados sobre los anuncios de ventas de automóviles')
hist_button = st.button('Construir histograma')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
