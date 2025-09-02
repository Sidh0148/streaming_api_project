def test_start_playback(client):
    response = client.post("/playback/start", params={"movie_id": 1, "username": "demo"})
    assert response.status_code == 200
    assert "Playback started" in response.json()["message"]


def test_stop_playback(client):
    response = client.post("/playback/stop", params={"movie_id": 1, "username": "demo"})
    assert response.status_code == 200
    assert "Playback stopped" in response.json()["message"]


def test_start_playback_invalid_user(client):
    response = client.post("/playback/start", params={"movie_id": 1, "username": "ghost"})
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
