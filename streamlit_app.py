# File
import streamlit as st

menu_items = {"Get help":"mailto:naveenkonam1985@gmail.com", "About":"Cemitek is a webiste POC for Cement Plant Design Calculations"}
st.set_page_config(page_title='Cemitek', page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=menu_items)

st.title("Cemitek")
st.write("Cement Plant Design")

with st.sidebar:
  st.write("Cemitek")
  tpd = st.text_input(label="Enter plant capacity")
  col1,col2 = st.columns([1,1])
  with col1:
    st.button("Calculate",key='calculate', use_container_width=True)
  with col2:
    st.button("Clear", key='clear', use_container_width=True)

