from config import db_params
from transform import transform_data
import psycopg2


cleaned_df = transform_data()
print(cleaned_df.head())
try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    print("Connected to the database")
    create_table_query = """
    CREATE TABLE IF NOT EXISTS weather_data(
        fecha DATE,
        hora TIME,
        pais VARCHAR(50),
        ciudad VARCHAR(50),
        temp_actual FLOAT,
        sensacion FLOAT,
        clima VARCHAR(50),
        descripcion VARCHAR(100),
        temp_min FLOAT,
        temp_max FLOAT,
        velocidad_viento FLOAT
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
except Exception as e:
    print(f"Error connecting to the database: {e}")
