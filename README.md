# 📘 Flask MongoDB CRUD API

A RESTful API built with **Flask**, **MongoDB**, and **Docker**, supporting full CRUD operations for user management.

## 🔗 Live Demo

> _You can deploy it using **Render**, **Railway**, or **Docker on VPS**. Link goes here if hosted._

---

## 📂 Project Structure

```
flask_mongo_crud/
│
├── app/
│   ├── __init__.py         # App factory
│   ├── config.py           # App config (Mongo URI, etc.)
│   ├── models/
│   │   └── user.py         # User model
│   ├── routes/
│   │   └── user_routes.py  # API route definitions
│   ├── schemas/
│   │   └── user_schema.py  # Marshmallow schema for validation
│   └── services/
│       └── user_service.py # Business logic for users
│
├── .env                    # MongoDB URI (excluded via .gitignore)
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── run.py                  # Entry point to start Flask app
```

---

## 📦 Features

- RESTful API using `Flask` + `Flask-RESTful`
- MongoDB database (via `Flask-PyMongo`)
- Input validation with `marshmallow`
- Secure password hashing using `Werkzeug`
- Dockerized for easy setup and deployment
- Modular architecture with services/models/routes
- Environment variable support with `python-dotenv`

---

## 🧪 API Endpoints

| Method | Endpoint           | Description              |
|--------|--------------------|--------------------------|
| GET    | `/users/`          | Get all users            |
| GET    | `/users/<id>`      | Get user by ID           |
| POST   | `/users/`          | Create a new user        |
| PUT    | `/users/<id>`      | Update existing user     |
| DELETE | `/users/<id>`      | Delete a user            |

---

## 🧰 Technologies Used

- **Backend**: Flask, Flask-PyMongo, Flask-RESTful, Marshmallow
- **Database**: MongoDB
- **Security**: Werkzeug (password hashing)
- **Containerization**: Docker, Docker Compose
- **Testing**: Pytest (optional)
- **Environment Handling**: python-dotenv

---

## ▶️ How to Run

### 🐳 With Docker

```bash
docker-compose up --build
```

Visit the API at: [http://localhost:5050/users](http://localhost:5050/users)

### 🖥️ Without Docker

```bash
# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export MONGO_URI="your-mongodb-uri"

# Run the server
python run.py
```

---

## ✏️ Example `curl` Commands

```bash
# Create a user
curl -X POST http://localhost:5050/users/ \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe","email":"john@example.com","password":"secure123"}'

# Get all users
curl http://localhost:5050/users/

# Get single user
curl http://localhost:5050/users/<id>

# Update user
curl -X PUT http://localhost:5050/users/<id> \
  -H "Content-Type: application/json" \
  -d '{"name":"Jane Doe"}'

# Delete user
curl -X DELETE http://localhost:5050/users/<id>
```

---

## 📄 License

<<<<<<< HEAD
This project is licensed under the MIT License.
=======
This project is licensed under the [MIT License](./LICENSE).
>>>>>>> fde0473 (Remove LICENSE file)
