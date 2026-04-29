import streamlit as st
import numpy as np

st.title("Clase 4 Numpy")
st.image("Logo.png",width=100)
st.sidebar.image("DMC.png")

valor=st.slider("Seleccione un valor",1,20)

arreglo=np.arange(valor)

st.write(arreglo)
