import pymysql

# Conexión a MySQL con pymysql (adpta los parámetros a tu servidor local)
def get_db_connection():
    return pymysql.connect(
        host="10.3.29.20",
        port=33060,
        user="user_agenda_db",
        password="usuario",
        database="agenda_db",
        cursorclass=pymysql.cursors.DictCursor  # Devuelve resultados como diccionarios
    )