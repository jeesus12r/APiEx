from app.models.user_model import User
from app import db
from flask import jsonify, request

def create_users(data):
    required_fields = ["nombre", "email", "password", "edad"]
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return {"msg": f"Faltan campos requeridos: {', '.join(missing_fields)}"}

    try:
        new_user = User(
            nombre=data["nombre"],
            email=data["email"],
            password=data["password"],
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

def update_users(user_id, data):
    user = User.query.get(user_id)
    if user:
        user.nombre = data.get("nombre", user.nombre)
        user.email = data.get("email", user.email)
        user.password = data.get("password", user.password)
        user.edad = data.get("edad", user.edad)
        db.session.commit()
        return {"msg": "Usuario actualizado exitosamente"}
    return {"msg": "Usuario no encontrado"}

def delete_users(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {"msg": "Usuario eliminado exitosamente"}
    return {"msg": "Usuario no encontrado"}

def login_users():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email y contraseña son requeridos"}), 400

    user = User.query.filter_by(email=email).first()

    if user:
        print(f"Usuario encontrado: {user.email}, Contraseña almacenada: {user.password}")
    else:
        print(f"Usuario con email '{email}' no encontrado.")

    if user and user.password == password:
        return jsonify({"message": "Inicio de sesión exitoso", "user": user.email}), 200
    elif user:
        return jsonify({"message": "Contraseña incorrecta"}), 401
    else:
        return jsonify({"message": "Email no encontrado"}), 401
