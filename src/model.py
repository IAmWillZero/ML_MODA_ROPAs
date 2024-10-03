import numpy as np
import cv2  # Asegúrate de importar cv2
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array

# Cargar el modelo preentrenado
model = ResNet50(weights='imagenet')

def classify_image(img_array):
    # Redimensionar la imagen para el modelo
    img_array = cv2.resize(img_array, (224, 224))  # Redimensionar para el modelo
    img_array = img_to_array(img_array)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Clasificación
    predictions = model.predict(img_array)
    return decode_predictions(predictions, top=1)[0][0][1]  # Retorna la etiqueta de la clase
