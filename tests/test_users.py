import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_create_user(client):
    response = client.post("/users/", json={
        "name": "Test User",
        "email": "test@example.com",
        "password": "testpass123"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert "email" in data and data["email"] == "test@example.com"
