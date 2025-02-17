import streamlit as st
from components.header import mostrar_header
from components.input_form import mostrar_input_form, clear_text
from components.result_table import mostrar_resultado
from services.api_service import consultar_cedula

# Cargar estilos CSS
with open("frontend/assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Mostrar el título
mostrar_header()

# Mostrar el formulario de entrada
cedula = mostrar_input_form()

#answer_placeholder = st.empty()

# Meti JavaScript para restringir la entrada de letras
st.markdown(
    """
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        const input = document.querySelector('input[type="text"]');
        if (input) {
            input.addEventListener('input', function(event) {
                // Eliminar letras del valor del input
                event.target.value = event.target.value.replace(/[^0-9]/g, '');
            });
        }
    });
    </script>
    """,
    unsafe_allow_html=True,
)

# Función para consultar la cédula
def ejecutar_consulta():
    if st.session_state.get("consultar_presionado", False):
        cedula = st.session_state.cedula_input
        if cedula and cedula.isdigit() and len(cedula) == 9:
            informacion = consultar_cedula(cedula)
            mostrar_resultado(informacion)
        elif cedula:
            st.warning("La cédula debe contener exactamente 9 dígitos numéricos.")

# Cro dos columnas para los botones
col1, col2 = st.columns(2)

# Botón para limpiar el input
with col1:
    if st.button("Limpiar", type="primary", on_click=clear_text):
        st.empty()

# Botón para consultar
with col2:
    if st.button("Consultar"):
        st.session_state.consultar_presionado = True  # Marcar que se presionó el botón
        st.rerun()

# Simular la acción de presionar Enter
if st.session_state.cedula_input and not st.session_state.get("consultar_presionado", False):
    st.session_state.consultar_presionado = True
    st.rerun()

if st.session_state.get("consultar_presionado", False):
    ejecutar_consulta()