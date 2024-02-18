import pandas as pd
import streamlit as st
import plotly.express as px

cars = pd.read_csv('vehicles_us.csv')

st.header('Análisis de vehículos y sus características')
st.write('La presente es una aplicación interactiva en la que se puede seleccionar diferentes características y así obtener gráficos representativos')
st.write('Los datos consignados fueron extraídos de la base de datos vehícles_us.csv')
hist_button = st.checkbox('Construir histograma')  # crear un botón
scatter_button = st.checkbox(
    'Construir gráfico de dispersión')  # crear segundo botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    figh = px.histogram(cars, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(figh, use_container_width=True)
if scatter_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
    figs = px.scatter(cars, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(figs, use_container_width=True)
