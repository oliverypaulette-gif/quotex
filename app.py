import streamlit as st
import time

# Intentamos importar pyautogui para el manejo del mouse
try:
    import pyautogui
    # Configuración de seguridad: si mueves el mouse a una esquina extrema, se detiene
    pyautogui.FAILSAFE = True
except ImportError:
    pyautogui = None

# Configuración de la página
st.set_page_config(
    page_title="Bot Automatización - Quotex",
    page_icon="⚡",
    layout="centered"
)

st.title("Panel de Control - Automatización Quotex")
st.write("Gestiona el envío automático de entradas a la plataforma.")

# Coordenadas configuradas
coord_x = 1229
coord_y = 438
coord_z = 485

st.subheader("Coordenadas actuales:")
col1, col2, col3 = st.columns(3)
col1.metric("Eje X", coord_x)
col2.metric("Eje Y", coord_y)
col3.metric("Acción / Z", coord_z)

st.divider()

# Opción de retraso para dar tiempo a posicionar la ventana de Quotex
delay = st.slider("Segundos de espera antes del clic:", min_value=0, max_value=5, value=2)

# Botón de acción principal conectado al mouse
if st.button("Ejecutar Entrada Automática", type="primary"):
    if pyautogui is None:
        st.error("Error: La librería 'pyautogui' no está instalada en el sistema.")
    else:
        with st.spinner(f"Esperando {delay} segundos... Prepárate."):
            time.sleep(delay)
        
        try:
            # Mueve el cursor a las coordenadas y hace clic izquierdo
            pyautogui.click(x=coord_x, y=coord_y)
            st.success(f"¡Clic ejecutado exitosamente en X={coord_x}, Y={coord_y}!")
        except Exception as e:
            st.error(f"Ocurrió un error al intentar hacer clic: {e}")
