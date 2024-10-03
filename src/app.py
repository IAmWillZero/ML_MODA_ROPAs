import streamlit as st
from PIL import Image
import numpy as np
from image_processing import get_dominant_color, create_color_image
from model import classify_image

def main():
    st.title("Clasificación de Ropa por Imágenes")

    # Modificar para permitir múltiples archivos
    uploaded_files = st.file_uploader("Sube imágenes de ropa", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    if uploaded_files:
        for uploaded_file in uploaded_files:
            try:
                # Cargar cada imagen
                image = Image.open(uploaded_file)
                st.image(image, caption=f"Imagen Cargada: {uploaded_file.name}", use_column_width=True)

                # Convertir imagen a formato necesario
                image_array = np.array(image)
                dominant_color = get_dominant_color(image_array)

                st.write("Color predominante (RGB):", dominant_color)

                # Crear y mostrar la imagen del color predominante
                color_image = create_color_image(dominant_color)
                st.image(color_image, caption="Color Predominante", use_column_width=True)

                # Clasificación de la imagen
                class_label = classify_image(image_array)
                st.write("Clasificación de la prenda:", class_label)

                # Mostrar la imagen con el color predominante superpuesto
                st.image(create_color_overlay(image_array, dominant_color), caption="Imagen con Color Predominante", use_column_width=True)

            except Exception as e:
                st.error(f"Error procesando la imagen {uploaded_file.name}: {str(e)}")

def create_color_overlay(image_array, dominant_color):
    """
    Crea una imagen con el color predominante superpuesto.
    """
    overlay = np.zeros_like(image_array)
    overlay[:, :] = dominant_color  # Asignar el color predominante
    # Superponer con cierta transparencia
    return Image.fromarray((image_array * 0.5 + overlay * 0.5).astype(np.uint8))

if __name__ == "__main__":
    main()
