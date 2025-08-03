import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Analisis de Anuncios de Vehiculos en EE.UU')

if st.button('Mostrar Histograma de Precio'):
    fig = px.histogram(df, x='price')
    st.write('Histograma de Precios de Vehiculos')
    st.plotly_chart(fig)

if st.button('Mostrar Gráfico de Dispersión de Año vs. Precio'):
    fig = px.scatter(df, x='model_year', y='price', color='condition')
    st.write('Gráfico de Dispersión entre Año del modelo vs. Precio')
    st.plotly_chart(fig)

