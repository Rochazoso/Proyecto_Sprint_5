import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
build_hist = st.checkbox('Construir histograma') # crear un botón

st.header('Venta de coches')

if build_hist: # al hacer clic en el botón
# escribir un mensaje
    st.header('Histograma de distribución de odometros de coches')
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_disper = st.checkbox("Construir gráfico de dispersión")

if build_disper:
    st.header("Dispersión de venta de precio de autos de acuerdo a odometros")
    st.write("Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches")

    fig_1 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión

    st.plotly_chart(fig_1, use_container_width=True) # crear gráfico de dispersión

