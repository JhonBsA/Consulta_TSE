import streamlit as st

def mostrar_header():
    st.markdown(
        """
        <style>
        .title {
            font-size: 36px !important;
            text-align: center;
            font-weight: bold;
            color: #1f77b4;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<p class="title">Consulta de Cédula - OMU</p>', unsafe_allow_html=True)