# import pandas as pd
# import plotly.express as px
# import streamlit as st
        
# car_data = pd.read_csv('vehicles_us.csv') # leer los datos
# hist_button = st.button('Construir histograma') # crear un botón
        
# if hist_button: # al hacer clic en el botón
# # escribir un mensaje
#     st.header('Venta de Autos')
#     st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
#             # crear un histograma
#     fig = px.histogram(car_data, x="odometer")
        
#             # mostrar un gráfico Plotly interactivo
#     st.plotly_chart(fig, use_container_width=True)

# disp_button = st.button("Construir gráfico de dispersión")

# if disp_button:
#     st.header("Dispersión de venta de autos")
#     st.write("Hola")

#     fig_1 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión

#     st.plotly_chart(fig_1, use_container_width=True) # crear gráfico de dispersión

import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para construir el gráfico de dispersión
disp_button = st.button("Construir gráfico de dispersión")

if disp_button:
    st.header("Dispersión de venta de autos")
    
    # Filtrar por precio
    min_price = st.slider("Precio mínimo", min_value=car_data['price'].min(), max_value=car_data['price'].max(), value=car_data['price'].min())
    max_price = st.slider("Precio máximo", min_value=car_data['price'].min(), max_value=car_data['price'].max(), value=car_data['price'].max())
    filtered_data = car_data[(car_data['price'] >= min_price) & (car_data['price'] <= max_price)]
    
    # Crear gráfico de dispersión
    fig = px.scatter(filtered_data, x="odometer", y="price")
    
    # Mostrar gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)
