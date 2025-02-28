# **ETL Pipeline con la API de OpenWeather**

## **Resumen de proyecto**

Este proyecto demuestra un pipeline ETL (Extract, Transform, Load) con datos meteorlógicos de una ciudad específica en un periodo determinado de tiempo. Los datos son extraídos desde una API externa, transformados (limpiados y procesados), y por último almacenados en una base de datos SQLite.
El objetivo del proyecto es brindar un dataset bien estructurado para futuros análisis o reportes.

## **Estructura del proyecto**
```
├── src
│   ├── extract.py        # código para extraer datos de la API
│   ├── transform.py      # código para limpieza y manipulación de datos
│   ├── load.py           # código para cargar datos en SQLite
│   ├── config.py         # configuración para la API KEY
├── requirements.txt      # librerias y dependencias necesarias
├── README.md             # Documentación del proyecto
└── run_etl.sh            # aplicación para ejecutar la pipeline.
```

## **Tecnologías**
- **Lenguaje de programación:** Python
- **Base de datos:** SQLite
- **API:** [openweathermap](https://openweathermap.org/api)

- **Librerias de python:**
  - `requests`
  - `pandas`
  - `SQLAlchemy`
  - `numpy`


## **Instalación**
1. Registrate en OpenWeather y obtén tu clave API.
2. Clona el repositorio: `git clone git@github.com:tu_nombre_de_usuario/etl_api_to_sql.git`
3. Crea un archivo `config.py` dentro de la carpeta "src" con el siguiente contenido:
   API_KEY = "tu_clave_aqui"
4. Instala dependencias: `pip install -r requirements.txt`

## Uso
Ejecuta el script principal: `python3 run_etl.py`