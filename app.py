import streamlit as st
import pandas as pd
import pydeck as pdk
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
    rgba='[0,204,0,160]'
elif sistype=='medio':
    level='Medio :large_yellow_circle:'
    delta='ML'
    rgba='[255,255,0,160]'
elif sistype=='alto':
    level='Alto :red_circle:'
    delta='-ML'
    rgba='[255,0,0,160]'
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

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=float(latitude),
        longitude=float(longitude),
        zoom=5,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[lon, lat]',
            get_color=rgba,
            get_radius=float(mag)*5000,
        ),
    ],
))
