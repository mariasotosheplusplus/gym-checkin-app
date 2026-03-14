import streamlit as st
import pandas as pd
import gspread
from datetime import datetime
from google.oauth2.service_account import Credentials

st.title("Check-in Gimnasio")

# -------- AUTENTICACIÓN --------

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=scope
)

gc = gspread.authorize(creds)

# -------- ABRIR SHEET --------

spreadsheet = gc.open("gimnasio")

usuarios_sheet = spreadsheet.worksheet("usuarios")
asistencias_sheet = spreadsheet.worksheet("asistencias")

# -------- LEER USUARIOS --------

usuarios = usuarios_sheet.get_all_records()
df_usuarios = pd.DataFrame(usuarios)

# -------- INPUT --------

id_unico = st.text_input("Ingresa tu IdUnico")

if st.button("Registrar asistencia"):

    if id_unico == "":
        st.warning("Ingresa tu IdUnico")

    else:

        usuario = df_usuarios[df_usuarios["IdUnico"] == int(id_unico)]

        if usuario.empty:

            st.error("Usuario no encontrado")

        elif not usuario.iloc[0]["Status"]:

            st.error("Membresía inactiva")

        else:

            nombre = usuario.iloc[0]["Nombre"]
            rutina = usuario.iloc[0]["Rutina"]

            ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # GUARDAR ASISTENCIA

            asistencias_sheet.append_row([
                int(id_unico),
                nombre,
                ahora
            ])

            st.success("Asistencia registrada")

            st.subheader(f"Bienvenido {nombre}")

            st.write("Rutina del día")

            st.info(rutina)
