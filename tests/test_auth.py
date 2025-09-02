import pytest


def test_login_success(client):
    response = client.post("/login", json={"username": "demo", "password": "demo123"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["access_token"].startswith("token-demo")

def test_login_failure(client):
    response = client.post("/login", json={"username": "wrong", "password": "wrong"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid username or password"


