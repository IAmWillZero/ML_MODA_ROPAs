import cv2
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image

def get_dominant_color(image, k=4):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    pixels = image.reshape(-1, 3)
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)
    dominant_color = kmeans.cluster_centers_.astype(int)[0]
    return tuple(dominant_color)

def create_color_image(color):
    """Crea una imagen de un solo color."""
    color_image = np.zeros((100, 100, 3), dtype=np.uint8)
    color_image[:] = color  # Asignar el color
    return Image.fromarray(color_image)
