import streamlit as st
import pandas as pd
from datetime import datetime

st.title("Check-in Gimnasio")

df = pd.read_csv("gimnasio.csv")

id_unico = st.text_input("Ingresa tu IdUnico")

if st.button("Registrar asistencia"):

    if id_unico == "":
        st.warning("Ingresa tu Id")

    else:

        id_unico = int(id_unico)

        usuario = df[df["IdUnico"] == id_unico]

        if usuario.empty:
            st.error("Usuario no encontrado")

        else:

            status = usuario.iloc[0]["Status"]

            if status == False:

                st.error("Membresía inactiva")

            else:

                nombre = usuario.iloc[0]["Nombre"]
                rutina = usuario.iloc[0]["Rutina"]

                ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                df.loc[df["IdUnico"] == id_unico, "Fecha"] = ahora

                df.to_csv("gimnasio.csv", index=False)

                st.success("Asistencia registrada")

                st.subheader(f"Bienvenido {nombre}")

                st.write("Rutina de hoy:")
                st.write(rutina)
else:
    st.write("Escanea tu QR para registrarte")
