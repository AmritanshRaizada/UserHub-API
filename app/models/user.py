from bson import ObjectId

class User:
    def __init__(self, name, email, password, _id=None):
        self.id = str(_id or ObjectId())
        self.name = name
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }
