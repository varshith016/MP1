import streamlit as st
import joblib
model = joblib.load('FOOD-INGREDIENTS')
st.title("FOOD & IT'S INGREDIENTS")
ip = st.text_input('Enter the food name')
op = model.predict([ip])
if st.button('Go'):
  st.title(op[0])
                 
      
