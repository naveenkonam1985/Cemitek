# File
import streamlit as st

menu_items = {"Get help":"mailto:naveenkonam1985@gmail.com", "About":"Cemitek is a webiste POC for Cement Plant Design Calculations"}
st.set_page_config(page_title='Cemitek', page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=menu_items)

st.title("Cemitek")
st.write("Cement Plant Design")

def capacities():
  st.session_state.calculate = True

def clear():
  st.session_state.calculate = False
  st.session_state.tpd = ""

if 'calculate' not in st.session_state:
    st.session_state.calculate = False

with st.sidebar:
  st.write("Cemitek")
  tpd_value = st.text_input(label="Enter plant capacity", key='tpd')
  col1,col2 = st.columns([1,1])
  
  with col1:
    st.button("Calculate",on_click=capacities, type='primary', use_container_width=True)
      
  with col2:
    st.button("Clear", on_click=clear, use_container_width=True)
  
  if st.session_state.calculate:
      if tpd_value is not None:
        st.write("Please Enter a value to proceed")
        

with st.container():
  plant_data = {}
  if st.session_state.calculate:
    if tpd_value:
      st.write(f"Entered TPD value is: {tpd_value}")
      tpd_value_corrected = int(tpd_value)
  
      plant_data['plant_capacity'] = (tpd_value_corrected * 330) / 1000000
  
      st.write(f"The plant capacity is: {plant_data['plant_capacity']} MTPA")
    

