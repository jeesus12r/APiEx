from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

# Crear la instancia de SQLAlchemy
db = SQLAlchemy()

def create_app():
    # Crear la instancia de Flask
    app = Flask(__name__)
    
    # Configurar las opciones de SQLAlchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = os.getenv("SECRET_KEY")
    
    # Inicializar SQLAlchemy con la aplicación
    db.init_app(app)
    
    # Configurar CORS
    CORS(app, resources={r"/*": {"origins": "http://localhost:5175"}})
    
    # Registrar los blueprints después de inicializar `db`
    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp)
    
    return app
