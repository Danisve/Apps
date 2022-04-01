import streamlit as st
st.title("mi primer app")
click=st.button("dale click")
st.write("el valor de click es:",click)

if click==true:
st.image("imagen")
#st.button("otro boton")
import pandas as pd
#df=pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')
#st.write(df)
#st.map(df)
#las siguientes lineas eran para ver ejemplos
st.text("holamundo")
st.text("la siguiente es una integral")
st.latex("\int_1^6 sin(x)dx")
st.markdown("#titulo")
st.markdown("**este es una viñeta**")
