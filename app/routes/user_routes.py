from flask import Blueprint, request, jsonify
from app.models.user_model import User
from app.controllers.user_controller import create_users as create_user, get_all_users, get_user_by_id, update_users as update_user, delete_users as delete_user, login_users

user_bp = Blueprint("user", __name__)

@user_bp.route("/users", methods=["POST"])
def add_user():
    data = request.json
    response = create_user(data)
    return jsonify(response)

@user_bp.route("/users", methods=["GET"])
def list_users():
    users = get_all_users()
    return jsonify(users)

@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    response = get_user_by_id(user_id)
    return jsonify(response)

@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
def remove_user(user_id):
    response = delete_user(user_id)
    return jsonify(response)

@user_bp.route("/login", methods=["POST", "OPTIONS"])
def login():
    if request.method == "OPTIONS":
        # Responder al preflight con un código HTTP 200
        response = jsonify({"message": "Preflight request successful"})
        response.status_code = 200
        return response
    return login_users()



