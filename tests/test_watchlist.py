import pytest


def test_add_to_watchlist(client):
    response = client.post("/watchlist", json={"user": "demo", "movie_id": 1})
    assert response.status_code == 200
    data = response.json()
    assert data["user"] == "demo"
    assert data["movie_id"] == 1

def test_get_watchlist(client):
    response = client.get("/watchlist/demo")
    assert response.status_code == 200
    watchlist = response.json()
    assert isinstance(watchlist, list)
    assert 1 in watchlist  # since we added movie_id=1 above

def test_add_to_watchlist_invalid_user(client):
    response = client.post("/watchlist", json={"user": "ghost", "movie_id": 1})
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


