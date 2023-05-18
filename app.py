import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

# Load the credentials from secrets.toml
creds = st.secrets["gcp"]

# Authorize the client with the retrieved credentials
client = gspread.service_account_from_dict(creds)

# Open the Google Sheet by its title or URL
sheet = client.open("Feedback usuario (respuestas)")

# Access the specific worksheet within the sheet
worksheet = sheet.get_worksheet(0)


st.title("Formulario de Sismo")
menu = ['Home', 'About']
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Formulario")

    with st.form(key='formulario'):
        fecha = datetime.datetime.now()
        formatted_datetime = fecha.strftime("%d/%m/%y %H:%M:%S")
        input1 = st.selectbox('Sentiste el ultimo sismo?', options=['Sí', 'No'])
        input2 = st.selectbox("Califica nuestros servicios (bajo 1 y alto 5)", options=['1', '2', '3', '4', '5'])
        input3 = st.selectbox('Compartirias nuestra aplicacion?', options=['Sí', 'No'])
        input4 = st.text_area('Algún comentario de mejora?')

        row = [formatted_datetime, input1, input2, input3, input4]
        boton = st.form_submit_button(label='Subir')

    if boton:
        st.success("Has subido tu informacion con exito")
        worksheet.append_row(row)
