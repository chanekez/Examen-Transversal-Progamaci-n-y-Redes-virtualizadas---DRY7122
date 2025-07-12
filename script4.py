from flask import Flask, request, redirect, render_template_string
import sqlite3
import hashlib
import os

app = Flask(__name__)
DB_NAME = 'usuarios.db'


def init_db():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)  
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            hash_contraseña TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def insertar_usuario():
    nombre = 'patricio pizarro'
    password = '1234segura'  
    hash_pass = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, hash_contraseña) VALUES (?, ?)", (nombre, hash_pass))
    conn.commit()
    conn.close()


def validar_usuario(nombre, contraseña):
    hash_pass = hashlib.sha256(contraseña.encode()).hexdigest()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND hash_contraseña = ?", (nombre, hash_pass))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None


@app.route('/', methods=['GET', 'POST'])
def login():
    mensaje = ""
    if request.method == 'POST':
        nombre = request.form['usuario']
        password = request.form['contraseña']
        if validar_usuario(nombre, password):
            mensaje = f'Bienvenido, {nombre}'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

    return render_template_string('''
        <h2>Login Examen DRY7122</h2>
        <form method="post">
            Usuario: <input type="text" name="usuario"><br>
            Contraseña: <input type="password" name="contraseña"><br>
            <input type="submit" value="Ingresar">
        </form>
        <p>{{ mensaje }}</p>
    ''', mensaje=mensaje)


if __name__ == '__main__':
    init_db()
    insertar_usuario()
    app.run(host='0.0.0.0', port=5800)

