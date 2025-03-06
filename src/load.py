from src.config import db_params
import psycopg2


def load_data(cleaned_df):
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS weather_data(
            fecha DATE,
            hora VARCHAR(50),
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

        for i, row in cleaned_df.iterrows():
            insert_query = """
            INSERT INTO weather_data(
            fecha, hora, pais, ciudad, temp_actual, sensacion,
            clima, descripcion, temp_min, temp_max, velocidad_viento)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(insert_query, tuple(row))
        conn.commit()

    except Exception as e:
        print(f"Error connecting to the database: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            print("Connection closed")
