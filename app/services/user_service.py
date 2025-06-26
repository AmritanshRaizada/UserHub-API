from flask import abort
from werkzeug.security import generate_password_hash
from .. import mongo
from bson.objectid import ObjectId
from ..models.user import User

def get_all_users():
    users = mongo.db.users.find()
    result = []
    for u in users:
        u["id"] = str(u["_id"])
        del u["_id"]
        result.append(u)
    return result

def get_user_by_id(user_id):
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        user["id"] = str(user["_id"])
        del user["_id"]
        return user
    return {}

def create_new_user(data):
    # Check if email already exists
    existing_user = mongo.db.users.find_one({"email": data["email"]})
    if existing_user:
        return {"error": "User with this email already exists."}, 409

    # Hash password
    data['password'] = generate_password_hash(data['password'])

    # Create user object
    user = User(**data)

    # Insert into DB
    mongo.db.users.insert_one(user.to_dict())

    # Return user dict (excluding _id)
    return user.to_dict()

def update_user_by_id(user_id, data):
    if "password" in data:
        data["password"] = generate_password_hash(data["password"])
    mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": data})
    return get_user_by_id(user_id)

def delete_user_by_id(user_id):
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    return {"msg": "User deleted"}
