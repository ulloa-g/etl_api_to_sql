from config import db_params
from transform import df
import psycopg2

try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    print("Connected to the database")
except Exception as e:
    print(f"Error connecting to the database: {e}")
