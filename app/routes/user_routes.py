from flask import Blueprint, request, jsonify
from ..services.user_service import *
from ..schemas.user_schema import UserSchema

user_bp = Blueprint("users", __name__)
user_schema = UserSchema()

@user_bp.route("/", methods=["GET"])
def get_users():
    return jsonify(get_all_users())

@user_bp.route("/<string:user_id>", methods=["GET"])
def get_user(user_id):
    return jsonify(get_user_by_id(user_id))

@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    return jsonify(create_new_user(data)), 201

@user_bp.route("/<string:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    errors = user_schema.validate(data, partial=True)
    if errors:
        return jsonify(errors), 400
    return jsonify(update_user_by_id(user_id, data))

@user_bp.route("/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return jsonify(delete_user_by_id(user_id))
