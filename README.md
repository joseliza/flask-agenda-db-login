# flask-agenda-db-login
Ejemplo muy básico de agenda de contactos creada con python y flask (contactos en una base de datos MySQL) y que permite registro de usuarios y login para entrar en nuestra aplicación.

Recuerda crear un entorno virtual llamado `.venv` y luego instalar Flask y las demás librerías con el comando pip.

Creamos entorno llamado .venv:
```bash
$ python3 -m venv .venv
```
Activamos el entorno (comando en Linux):
```bash
$ source .venv/bin/activate
```
Instalamos **flask**, **pymysql** y **werkzeug**:
```bash
(.venv)$ pip install flask werkzeug
```
O bien podéis instalar los paquetes que hay dentro del archivo ```requirements.txt```

```bash
(.venv)$ pip install -r requirements.txt
```

## Las tablas usadas en la base datos son:

### contactos
Tabla que almacena los contactos de la agenda:
```sql
CREATE TABLE contactos (
  id int NOT NULL AUTO_INCREMENT,
  nombre varchar(50) NOT NULL,
  telefono varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
)
```

### usuarios
Tabla que almacena los usuarios que se registran en la aplicación:
```sql
CREATE TABLE usuarios (
  username varchar(45) NOT NULL,
  name varchar(255) NOT NULL,
  surname varchar(255) DEFAULT NULL,
  email varchar(320) NOT NULL,
  password_hash varchar(255) NOT NULL,
  PRIMARY KEY (`username`)
)
```
