import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
import random

st.title("💖➡️🌸 Toca la Flor para Cambiar de Color")

# Estado de color (se guarda entre interacciones)
if "color" not in st.session_state:
    st.session_state.color = "#ff69b4"  # Color inicial rosa

# Generador de colores aleatorios
def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# Si se toca la flor, cambia de color
if st.button(" "):  # Botón invisible
    st.session_state.color = random_color()

# Contenedor de la animación
placeholder = st.empty()

def heart_shape(t):
    """Genera las coordenadas de un corazón"""
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x / 5, y / 5  # Reducimos el tamaño

def flower_shape(t, scale=1):
    """Genera las coordenadas de una flor con pétalos que cambian"""
    r = 1 + scale * np.sin(6 * t)  # 6 controla el número de pétalos
    x = r * np.cos(t)
    y = r * np.sin(t)
    return x, y

# Generar puntos base
t = np.linspace(0, 2 * np.pi, 100)

# Animación de transformación
for i in range(50):  
    alpha = i / 50  # Progresión de 0 a 1
    x_heart, y_heart = heart_shape(t)
    x_flower, y_flower = flower_shape(t, scale=alpha)

    # Interpolación entre corazón y flor
    x = (1 - alpha) * x_heart + alpha * x_flower
    y = (1 - alpha) * y_flower + alpha * y_flower

    # Dibujar
    fig, ax = plt.subplots()
    ax.plot(x, y, color=st.session_state.color, linewidth=2)
    ax.fill(x, y, color=st.session_state.color, alpha=0.6)
    ax.set_aspect('equal')
    ax.axis('off')

    # Mostrar en Streamlit
    placeholder.pyplot(fig)
    time.sleep(0.1)  # Control de velocidad
