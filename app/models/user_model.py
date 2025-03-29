from flask_sqlalchemy import SQLAlchemy
from app import db  # Mantener esto aquí está bien si no causa ciclos.


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=True)

    def __init__(self, email, password, nombre=None, edad=None):
        self.email = email
        self.password = password
        self.nombre = nombre
        self.edad = edad
