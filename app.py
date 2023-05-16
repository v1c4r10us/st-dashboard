import streamlit as st
from PIL import image

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

# Design
st.set_page_config(page_title="Alertas Sismicas",
                   page_icon="bar_chart:",
                   layout="wide")

header_style = """
    <style>
        .header {
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: red;
            color: white;
            padding: 20px;
            font-size: 24px;
            font-weight: bold;
            border-radius: 15px;
        }

        .header .image {
            width: 40px;
            height: 40px;
            margin-right: 10px;
        }

        .header span {
            font-size: 48px;
        }
    </style>
"""

# Picture paths
icono1 = Image.open('src/alert_icon.png')

# Display the header
st.markdown(header_style, unsafe_allow_html=True)
st.markdown(
    f'''
    <div class="header">
        <div class="image">
            <img src="{icono1}" alt="Alert Icon">
        </div>
        <span>ALERTA DE SISMO FUERTE</span>
        <div class="image">
            <img src="{icono1}" alt="Alert Icon">
        </div>
    </div>
    ''',
    unsafe_allow_html=True
)

split_markdown_style = """
    <style>
        .split-markdown {
            display: flex;
            justify-content: center;
        }
        .left-section {
            width: 400px;
            background-color: teal;
            padding: 20px;
            text-align: center;
            border-radius: 15px;
            margin-right: 20px;
        }
        .right-section {
            width: 400px;
            background-color: orange;
            padding: 20px;
            text-align: center;
            border-radius: 15px;
            margin-left: 20px;
        }
        .split-markdown h2 {
            font-size: 80px;
            color: black;
        }
        .split-markdown p {
            font-size: 44px;
            color: black;
        }
        
    </style>
"""

# Display the split Markdown sections
st.markdown(split_markdown_style, unsafe_allow_html=True)
st.markdown(
    '''
    <div class="split-markdown">
        <div class="left-section">
            <h2>3.5</h2>
            <p>MAGNITUD</p>
        </div>
        <div class="right-section">
            <h2>12KM</h2>
            <p>PROFUNDIDAD</p>
        </div>
    </div>
    ''',
    unsafe_allow_html=True
)
