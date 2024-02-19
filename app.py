import streamlit as st
import pandas as pd
import plotly_express as px


# Se carga el dataset de interés
data = pd.read_csv('vehicles_us.csv')
# Creacion del header de la página
st.header('Datos recabados sobre los anuncios de ventas de automóviles',
          divider='rainbow')
# Creacion del subheader
st.subheader('Seleccione el tipo de gráfico que desea ver:')
# Creación de las checkbox con las opciones disponibles.
hist_box = st.checkbox(
    'Distribución de los vehículos por año del modelo.')
disp_box_price = st.checkbox(
    'Precio del automóvil en función del año del modelo.')
disp_box_odo = st.checkbox(
    'Medida del odómetro en función del año del modelo.')
st.write('En todas las opciones podrá escoger la condición del automóvil que le interese analizar.')
st.divider()

if hist_box:
    st.subheader(
        'Histograma sobre los modelos por año disponibles dependiendo de la condición del automóvil.')

    st.write('Puede seleccionar la condición del automóvil que desee ver u ocultar.')

    fig = px.histogram(data, x='model_year', color='condition', labels=dict(
        model_year="Año del modelo", count="Frecuencia", condition="Condición"))
    fig.update_layout(
        title='Año del modelo.')

    st.plotly_chart(fig, use_container_width=True)

if disp_box_price:
    st.subheader('Gráfico de dispersión del precio por año del modelo.')

    st.write('Puede seleccionar la condición del automóvil que desee ver u ocultar.')

    fig = px.scatter(data, x="model_year", y="price", color='condition',
                     labels=dict(model_year="Año del modelo", price="Precio ($)", condition="Condición"))
    fig.update_layout(
        title='Precio del vehículo dependiendo del año del modelo')

    st.plotly_chart(fig, use_container_width=True)

if disp_box_odo:
    st.subheader(
        'Gráfico de dispersión de la medición del odómetro por año del modelo.')

    st.write('Puede seleccionar la condición del automóvil que desee ver u ocultar.')

    fig = px.scatter(data, x='model_year', y='odometer', color='condition',
                     labels=dict(model_year="Año del modelo", odometer="Medición del odómetro (Distancia)", condition="Condición"))
    fig.update_layout(
        title='Medición del odómetro en función del año del modelo.')

    st.plotly_chart(fig, use_container_width=True)

else:
    st.write('\n\n\t Ningún gráfico ha sido seleccionado.')
