import pytest


def test_get_movies_schema(client):
    response = client.get("/movies")
    assert response.status_code == 200
    movies = response.json()
    for movie in movies:
        assert "id" in movie
        assert "title" in movie
        assert "genre" in movie
        assert "year" in movie


def test_get_movie_not_found(client):
    response = client.get("/movies/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Movie not found"

