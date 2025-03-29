from app import db

class User(db.Model):
    __tablename__ = 'users'  # Especificar explícitamente el nombre de la tabla para mayor claridad
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)  # Ajusté el tamaño para alinearlo con la estructura SQL
    password = db.Column(db.String(255), nullable=False)  # Ajusté el tamaño para coincidir con la tabla creada
    nombre = db.Column(db.String(100), nullable=True)
    edad = db.Column(db.Integer, nullable=True)

    def __init__(self, email, password, nombre=None, edad=None):
        self.email = email
        self.password = password
        self.nombre = nombre
        self.edad = edad
