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
<<<<<<< HEAD
    # Check for duplicate email
=======

>>>>>>> fde0473 (Remove LICENSE file)
    existing_user = mongo.db.users.find_one({"email": data["email"]})
    if existing_user:
        return {"error": "User with this email already exists."}, 409

    data['password'] = generate_password_hash(data['password'])
    user = User(**data)
    mongo.db.users.insert_one(user.to_dict())
    return user.to_dict()
    data['password'] = generate_password_hash(data['password'])
    user_doc = {
        "name": data["name"],
        "email": data["email"],
        "password": data["password"]
    }
    result = mongo.db.users.insert_one(user_doc)
    user_doc["id"] = str(result.inserted_id)
    return user_doc

def update_user_by_id(user_id, data):
    mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": data})
    return get_user_by_id(user_id)

def delete_user_by_id(user_id):
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    return {"msg": "User deleted"}
