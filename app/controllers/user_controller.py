from app.models.user_model import User
from app import db

def create_user(data):
    try:
        new_user = User(
            nombre=data["nombre"],
            email=data["email"],
            password=data["password"],  # Directamente guarda la contraseña
            edad=data["edad"]
        )
        db.session.add(new_user)
        db.session.commit()
        return {"msg": "Usuario creado exitosamente"}
    except Exception as e:
        return {"msg": "Error al crear usuario", "error": str(e)}

def get_all_users():
    users = User.query.all()
    return [{"id": u.id, "nombre": u.nombre, "email": u.email, "edad": u.edad} for u in users]

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        return {"id": user.id, "nombre": user.nombre, "email": user.email, "edad": user.edad}
    return {"msg": "Usuario no encontrado"}

def update_user(user_id, data):
    user = User.query.get(user_id)
    if user:
        user.nombre = data.get("nombre", user.nombre)
        user.email = data.get("email", user.email)
        user.password = data.get("password", user.password)  # Permite actualizar la contraseña
        user.edad = data.get("edad", user.edad)
        db.session.commit()
        return {"msg": "Usuario actualizado exitosamente"}
    return {"msg": "Usuario no encontrado"}

def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {"msg": "Usuario eliminado exitosamente"}
    return {"msg": "Usuario no encontrado"}

from flask import jsonify, request

def login_user():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    # Validar si los campos no están vacíos
    if not email or not password:
        return jsonify({"message": "Email y contraseña son requeridos"}), 400

    # Buscar el usuario por email
    user = User.query.filter_by(email=email).first()

    # Depuración: verificar si se encontró el usuario
    if user:
        print(f"Usuario encontrado: {user.email}, Contraseña almacenada: {user.password}")
    else:
        print(f"Usuario con email '{email}' no encontrado.")

    # Comparar contraseña (directa en este caso)
    if user and user.password == password:
        return jsonify({"message": "Inicio de sesión exitoso", "user": user.email}), 200
    elif user:
        return jsonify({"message": "Contraseña incorrecta"}), 401
    else:
        return jsonify({"message": "Email no encontrado"}), 401
