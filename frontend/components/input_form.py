import streamlit as st

def clear_text():
    st.session_state["cedula_input"] = ""

def mostrar_input_form_nacional():
    #Muestra el campo de entrada
    cedula = st.text_input(
        "Ingrese solo números (máximo 9 dígitos)",
        max_chars=9,
        key="cedula_input",
        help="Se aceptan unicamente números",
        placeholder="Digite el número de cédula",
    )

    return cedula
