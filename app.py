import streamlit as st

# Design
st.set_page_config(page_title="Alertas Sismicas",
                   page_icon="bar_chart:",
                   layout="wide")

result=st.experimental_get_query_params() #Get params of url

country=result['val'][0]
latitude=result['val'][1]
longitude=result['val'][2]
depth=result['val'][3]
mag=result['val'][4]
sistype=result['val'][5]

# Creating layout

if sistype=='leve':
    level='󰕿 Leve'
elif sistype=='medio':
    level=' Medio'
elif sistype=='alto':
    level=' Alto'
else:
    level='? Unknown'
st.markdown('# Alerta de nivel: '+level)
