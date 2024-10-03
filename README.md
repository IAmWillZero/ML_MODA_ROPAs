# Fashion Analysis

Este proyecto analiza las preferencias de color en imágenes de ropa utilizando programación orientada a objetos y visualización interactiva con Streamlit.

## Descripción

La aplicación permite a los usuarios buscar imágenes de ropa en la API de Pexels y analizar los colores predominantes en estas imágenes. Los resultados se presentan de manera interactiva en un navegador web.

## Estructura del Proyecto

- `data/`: Contiene los datos de salida del análisis.
- `src/`: Código fuente del programa.
  - `app.py`: Aplicación principal de Streamlit.
  - `image_fetcher.py`: Clase para obtener imágenes de la API.
  - `color_analyzer.py`: Clase para analizar colores.
  - `fashion_item.py`: Clase que representa un artículo de moda.
  - `fashion_analysis.py`: Clase que coordina el análisis de moda.
- `requirements.txt`: Dependencias del proyecto.
- `README.md`: Documentación del proyecto.
- `.gitignore`: Archivos y carpetas a ignorar en Git.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd fashion_analysis
    ```

2. Crea un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Asegúrate de tener una clave de API de Pexels. Regístrate en [Pexels](https://www.pexels.com/) para obtenerla.
2. Ejecuta la aplicación Streamlit:
    ```bash
    streamlit run src/app.py
    ```
3. Abre el navegador y navega a la dirección que te indique Streamlit (generalmente `http://localhost:8501`).

## Contribución

Si deseas contribuir, por favor crea un fork del repositorio y envía un pull request con tus cambios.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más información.
