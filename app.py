import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
# escribir un mensaje
    st.header('Venta de Autos')
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    options = car_data["price"].unique().tolist()
    options_1 = car_data["odometer"].unique().tolist()
    year = st.selectbox('Which one do you want to see?', options, options_1 0)
    car_data = car_data[car_data['price'] =price]
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button("Construir gráfico de dispersión")

if disp_button:
    st.header("Dispersión de venta de autos")
    st.write("Hola")

    fig_1 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig_1, use_container_width=True) # crear gráfico de dispersión