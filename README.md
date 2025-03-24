# SongRecommender

Este proyecto implementa un sistema de recomendación de canciones utilizando el algoritmo KNN (K-Nearest Neighbors) y clustering. El sistema permite buscar canciones y obtener recomendaciones basadas en características musicales como tempo, bailabilidad, volumen, etc.

## Características

- Búsqueda de canciones por nombre
- Visualización detallada de características musicales
- Sistema de recomendación basado en KNN
- Clustering de canciones para mejorar la precisión y velocidad de las recomendaciones
- Interfaz web intuitiva y responsive

## Tecnologías Utilizadas

- Python 3.x
- Flask (Backend)
- Pandas (Procesamiento de datos)
- Scikit-learn (Machine Learning)
- HTML/CSS/JavaScript (Frontend)

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/SongRecommender.git
cd SongRecommender
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Asegúrate de tener el archivo de datos procesados en la carpeta `data/datos_procesados.csv`

## Uso

1. Inicia el servidor Flask:
```bash
cd backend
python app_flask.py
```

2. Abre el archivo `frontend/index.html` en tu navegador

3. Busca una canción y obtén recomendaciones basadas en sus características musicales

## Estructura del Proyecto

```
SongRecommender/
├── backend/
│   ├── app_flask.py
│   └── recommender.py
├── frontend/
│   └── index.html
├── data/
│   ├── limpieza_datos.ipynb
│   └── datos_procesados.csv
└── requirements.txt
```

## Proceso de Datos

### Limpieza y Preprocesamiento
El sistema incluye un proceso de limpieza de datos (`limpieza_datos.ipynb`) que:
- Elimina valores nulos y duplicados
- Normaliza las características numéricas
- Preserva los valores originales para visualización
- Aplica clustering para agrupar canciones similares

### Clustering
Para mejorar la eficiencia y precisión de las recomendaciones:
- Las canciones se agrupan en clusters basados en sus características musicales
- Las recomendaciones se buscan solo dentro del mismo cluster
- Esto reduce significativamente el tiempo de búsqueda y mejora la relevancia de las recomendaciones

## Características Musicales

El sistema utiliza las siguientes características para las recomendaciones:
- Año de lanzamiento
- Popularidad
- Duración (duration_ms)
- Volumen (loudness)
- Tempo (BPM)
- Bailabilidad (danceability)
- Acústica (acousticness)
- Instrumentalidad (instrumentalness)
- En vivo (liveness)
- Habla (speechiness)

Cada característica aporta una dimensión única a la similitud entre canciones:
- **Bailabilidad**: Mide qué tan adecuada es la canción para bailar
- **Acústica**: Indica qué tan acústica es la canción
- **Instrumentalidad**: Mide la ausencia de voces
- **En vivo**: Indica la probabilidad de que la canción sea en vivo
- **Habla**: Mide la presencia de palabras habladas

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría hacer.

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles. 