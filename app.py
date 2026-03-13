
import streamlit as st
import pandas as pd
from datetime import datetime

usuarios = pd.DataFrame({
    "id_usuario":[101,102,103],
    "nombre":["Ana","Luis","Maria"],
    "membresia_activa":[True,True,False]
})

rutinas = pd.DataFrame({
    "id_usuario":[101,102,103],
    "rutina":[
        "Pierna: Sentadilla 4x10 / Prensa 4x12",
        "Pecho: Press banca 4x8 / Aperturas 3x12",
        "Espalda: Dominadas 4x6 / Remo 4x10"
    ]
})

st.title("Check-in Gimnasio")

id_usuario = st.query_params.get("id")

if id_usuario:

    id_usuario = int(id_usuario)

    usuario = usuarios[usuarios.id_usuario == id_usuario]

    if len(usuario)==0:
        st.error("Usuario no encontrado")

    else:

        nombre = usuario.iloc[0]["nombre"]
        activo = usuario.iloc[0]["membresia_activa"]

        st.write("Bienvenido", nombre)

        if not activo:
            st.error("Membresía vencida")

        else:

            st.success("Asistencia registrada")

            rutina = rutinas[rutinas.id_usuario == id_usuario].iloc[0]["rutina"]

            st.subheader("Rutina de hoy")
            st.write(rutina)

else:
    st.write("Escanea tu QR para registrarte")
