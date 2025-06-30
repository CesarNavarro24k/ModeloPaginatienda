from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from .models.ModeloLibro import ModeloLibro
from .models.ModeloUsuario import ModeloUsuario
from .models.entities.Usuario import Usuario
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)
csrf = CSRFProtect()
db = MySQL(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = Usuario(
            None, request.form["usuario"],
            request.form["password"],
            None)
        usuario_logeado = ModeloUsuario.login(db, usuario)
        if usuario_logeado != None:
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

# @app.route("/password/<password>")
# def encriptar_password(password):
#     encriptado = generate_password_hash(password)
#     coincide = check_password_hash(encriptado, password)
#     return "Encriptado: {0} | Coindice {1}".format(encriptado, coincide)


@app.route("/libros")
def listar_libros():
    try:
        libros = ModeloLibro.listar_libros(db)
        data = {
            'Libros': libros
        }
        return render_template("listado_libros.html", data=data)

    except Exception as ex:
        print(ex)


def pagina_no_encontrada(error):
    return render_template("errores/404.html"), 404


def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(404, pagina_no_encontrada)
    return app
