import streamlit as st
import pandas as pd
import numpy as np
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
    level='Leve :large_green_circle:'
    delta='ML'
elif sistype=='medio':
    level='Medio :large_yellow_circle:'
    delta='ML'
elif sistype=='alto':
    level='Alto :red_circle:'
    delta='-ML'
else:
    level=':white_circle: Desconocido'
    delta='ML'
st.markdown('# Nivel de alerta: '+level) #Level
st.markdown('***')
d={'lat':[float(latitude)], 'lon':[float(longitude)]}
df=pd.DataFrame(d)
col1,col2=st.columns(2)
col1.metric(label='Magnitud', value=mag, delta=delta)
col2.metric(label='Profundidad', value=depth, delta='Km')
st.map(df, zoom=-1)
