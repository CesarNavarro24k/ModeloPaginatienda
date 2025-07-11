from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Usuario(UserMixin):

    def __init__(self, id, usuario, password, tipousuario):
        self.id = id
        self.usuario = usuario
        self.password = password
        self.tipousuario = tipousuario

    def encriptar_password(password):
        encriptado = generate_password_hash(password)
        coincide = check_password_hash(encriptado, password)
        return f" |Coincide: {coincide} "
