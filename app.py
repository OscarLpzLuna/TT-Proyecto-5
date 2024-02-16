import streamlit as st
import pandas as pd
import plotly_express as px


# Se carga el dataset de interés
data = pd.read_csv('../vehicles_us.csv')

st.header('Datos recabados sobre los anuncios de automóviles')
