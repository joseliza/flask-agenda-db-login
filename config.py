import os   
from dotenv import load_dotenv
import pymysql

# Cargar variables de entorno. Si no están definidas, las carga desde el archivo .env
if not os.getenv("DOCKER_ENV"):
    load_dotenv()

# Variables de entorno, por si no están definidas
DB_HOST = os.getenv('DB_HOST', '10.3.29.20')
DB_PORT = os.getenv('DB_PORT', 33060)
DB_USER = os.getenv('DB_USER', 'user_agenda_db')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'usuario')
DB_NAME = os.getenv('DB_NAME', 'agenda_db')
SECRET_KEY = os.getenv('SECRET_KEY', 'clave_secreta')

# Conexión a MySQL con pymysql
def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        port=int(DB_PORT),
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor  # Devuelve resultados como diccionarios
    )