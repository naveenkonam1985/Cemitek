# File
import streamlit as st

menu_items = {"Get help":"", "About":"Cemitek is a sample webiste"}
st.set_page_config(page_title='Cemitek', page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=menu_items)

st.title("Cemitek")
st.write("Cement Plant Design")


