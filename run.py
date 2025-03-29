from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()  # Crea las tablas en la base de datos

if __name__ == "__main__":
    app.run(debug=True, port=3000)  # Ejecutar en el puerto 3000
