from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde un archivo .env
load_dotenv()

# Crear la instancia de SQLAlchemy
db = SQLAlchemy()

def create_app():
    # Crear la instancia principal de Flask
    app = Flask(__name__)

    # Configuración de la base de datos con variables de entorno
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Configuración de seguridad para la aplicación
    app.secret_key = os.getenv("SECRET_KEY")

    # Inicializar la instancia de SQLAlchemy con la aplicación Flask
    db.init_app(app)

    # Configuración de CORS para permitir solicitudes desde el frontend
    CORS(app, resources={r"/*": {"origins": "http://localhost:5175"}})

    # Registrar los blueprints después de inicializar la base de datos
    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix="/api")

    return app
