import streamlit as st

def mostrar_resultado(informacion):
    if informacion:
        st.write("Información obtenida:")
        st.table({
            "Cédula": [informacion['cedula']],
            "Nombre Completo": [informacion['nombre_completo']],
            "Fecha de Nacimiento": [informacion['fecha_nacimiento']],
            "Provincia": [informacion['provincia']]
        })
    else:
        st.error("No se pudo obtener información para la cédula proporcionada.")