from flask import Flask, render_template, request, session, redirect, url_for
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash
from config import get_db_connection, SECRET_KEY

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = SECRET_KEY

@app.route('/')
def index():
    return render_template('index.html', username=session.get('username'))

@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username, password = request.form['username'], request.form['password']

        # Conectar y verificar credenciales
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT password_hash FROM usuarios WHERE username = %s", (username))
            user = cursor.fetchone()
        connection.close()

        # Si el usuario existe y la contraseña es correcta, iniciar sesión
        if user and check_password_hash(user['password_hash'], password):
            session['username'] = username
            return redirect(url_for('home'))
        return render_template('login.html', mensaje="Usuario o contraseña incorrectos.")

    return render_template('login.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/registro', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username, name, surname, email, password = request.form['username'], request.form['name'], request.form['surname'], request.form['email'], request.form['password']
        password_hash = generate_password_hash(password)

        connection = get_db_connection()
        with connection.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO usuarios (username, name, surname, email, password_hash) VALUES (%s, %s, %s, %s, %s)", (username, name, surname, email, password_hash))
                connection.commit()
            except pymysql.err.IntegrityError:
                return render_template('registro.html', mensaje="El usuario ya existe.")
        connection.close()

        return redirect(url_for('login'))

    return render_template('registro.html')

@app.route("/listar")
def listar():
    username = None
    if 'username' in session:
        username = session['username']
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT nombre, telefono FROM contactos order by nombre asc")
        contactos = cursor.fetchall()
    connection.close()
    return render_template("listar.html", contactos=contactos, username=username)
    

@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    username = None
    mensaje=""
    resultado = {}

    if 'username' in session:
            username = session['username']
    if request.method == "POST":
        nombre = request.form["nombre"]
        if nombre:
            connection = get_db_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT nombre, telefono FROM contactos where nombre = %s", (nombre))
                contactos = cursor.fetchall()
                if len(contactos) == 0:
                    mensaje = "Contacto no encontrado."
                connection.close()
                resultado = contactos
         
    return render_template("buscar.html", resultado=resultado, mensaje=mensaje, username=username)

@app.route("/insertar", methods=["GET", "POST"])
def insertar():
    username = None
    mensaje = ""

    if 'username' in session:
            username = session['username']

    if request.method == "POST":
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("insert into contactos (nombre, telefono) values (%s, %s)", (nombre, telefono))
            mensaje = f"Contacto {nombre} insertado."
        connection.commit()
        connection.close()

    return render_template("insertar.html", mensaje=mensaje, username=username)

@app.route("/borrar", methods=["GET", "POST"])
def borrar():
    username = None
    mensaje = ""

    if 'username' in session:
            username = session['username']

    if request.method == "POST":
        nombre = request.form["nombre"]
        if nombre:
            connection = get_db_connection()
            # Existe el contacto?
            with connection.cursor() as cursor:
                cursor.execute("SELECT nombre, telefono FROM contactos where nombre = %s", (nombre))
                contactos = cursor.fetchall()
            if len(contactos) == 0:
                mensaje = "Contacto no encontrado."
            else:
                # Existe, borrar
                with connection.cursor() as cursor:
                    cursor.execute("delete from contactos where nombre = %s", (nombre))
                    mensaje = f"Contacto {nombre} eliminado."
                connection.commit()
                connection.close()            

    return render_template("borrar.html", mensaje=mensaje, username=username)

if __name__ == "__main__":
    app.run(debug=True)
