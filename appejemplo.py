import streamlit as st
st.title("mi primer app")
click=st.button("dale click")
st.write("el valor de click es:",click)

if click==True:
    st.image("imagen.jpg")

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
numl = st.slider('elige un numero 1', 0, 130, 25)
num2 = st.slider('elige un numero 2', 0, 130, 25)
suma= num1+num2
st.write ("la suma de",num1,"y",num2,"es:",suma)
st.write("ahora multipliquemos")
nn1 = st.number_input("dame n1")
nn2 = st.number_input("dame n2")
mult=nn1*nn2
st.write("la multiplicacion de" ,nn1, "y" ,nn2, "es:", mult)
with st.sidebar:
    num1=st.slider('elige el numero1', 0,130,25)
    num2=st.slider('elige el numero1', 0,130,25)
    st.write("la suma de los dos es", suma)
    