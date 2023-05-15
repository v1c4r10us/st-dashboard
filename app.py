import streamlit as st

result=st.experimental_get_query_params() #Get params of url

country=result['val'][0] #Country
latitude=result['val'][1]
longitude=result['val'][2]
depth=result['val'][3]
mag=result['val'][4]
sistype=result['val'][5]

st.title(country)
st.text('Latitud: '+latitude)
st.text('Longitud: '+longitude)
st.text('Profundidad: '+depth)
st.text('Magnitud: '+mag)
st.text('Tipo: '+sistype)

