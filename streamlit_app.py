# File
import streamlit as st

menu_items = {"Get help":"mailto:naveenkonam1985@gmail.com", "About":"Cemitek is a webiste POC for Cement Plant Design Calculations"}
st.set_page_config(page_title='Cemitek', page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=menu_items)

st.title("Cemitek")
st.write("Cement Plant Design")

with st.container():
  col1,col2 = st.columns([1,1])

  with col1:
    with st.form("my_form"):
     st.write("Design Parameters")
     kiln_tpd = st.text_input("Kiln Capacity")
     kiln_running_days = st.text_input("Kiln Running Days") 
     # Every form must have a submit button.
     submitted = st.form_submit_button("Submit")
     
       
  with col2:
    if submitted:
      st.write("Form Submitted")
      plant_capacity = int(kiln_tpd) * int(kiln_running_days)
      st.write(f"Plant Capacity {plant_capacity} MTPA")

      

