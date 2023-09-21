# File
import streamlit as st

menu_items = {"Get help":"mailto:naveenkonam1985@gmail.com", "About":"Cemitek is a webiste POC for Cement Plant Design Calculations"}
st.set_page_config(page_title='Cemitek', page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=menu_items)

st.title("Cemitek")
st.write("Cement Plant Design")

with st.sidebar:
  st.write("Cemitek")
  tpd = st.text_input("Enter plant capacity to calculate the parameters")
  col1,col2 = st.columns([1,1])
  with col1:
    st.button("Click Me",use_container_width=True)
  with col2:
    st.button("Clear", use_container_width=True)

