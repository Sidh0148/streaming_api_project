from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Mock Streaming API", version="1.0")

# -----------------------
# Data Models
# -----------------------
class UserLogin(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class Movie(BaseModel):
    id: int
    title: str
    genre: str
    year: int

class WatchlistItem(BaseModel):
    user: str
    movie_id: int

# -----------------------
# Fake Data
# -----------------------
fake_users = {
    "demo": {"password": "demo123", "watchlist": []}
}

fake_movies = [
    {"id": 1, "title": "Inception", "genre": "Sci-Fi", "year": 2010},
    {"id": 2, "title": "The Dark Knight", "genre": "Action", "year": 2008},
    {"id": 3, "title": "Interstellar", "genre": "Sci-Fi", "year": 2014},
]

# -----------------------
# Endpoints
# -----------------------
@app.post("/login", response_model=TokenResponse)
def login(user: UserLogin):
    if user.username in fake_users and fake_users[user.username]["password"] == user.password:
        return {"access_token": f"token-{user.username}"}
    raise HTTPException(status_code=401, detail="Invalid username or password")

@app.get("/movies", response_model=List[Movie])
def get_movies(genre: Optional[str] = None):
    if genre:
        return [m for m in fake_movies if m["genre"].lower() == genre.lower()]
    return fake_movies

@app.get("/movies/{movie_id}", response_model=Movie)
def get_movie(movie_id: int):
    movie = next((m for m in fake_movies if m["id"] == movie_id), None)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@app.post("/watchlist", response_model=WatchlistItem)
def add_to_watchlist(item: WatchlistItem):
    if item.user not in fake_users:
        raise HTTPException(status_code=404, detail="User not found")
    fake_users[item.user]["watchlist"].append(item.movie_id)
    return item

@app.get("/watchlist/{username}", response_model=List[int])
def get_watchlist(username: str):
    if username not in fake_users:
        raise HTTPException(status_code=404, detail="User not found")
    return fake_users[username]["watchlist"]

@app.post("/playback/start")
def start_playback(movie_id: int, username: str):
    if username not in fake_users:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"Playback started for movie {movie_id} by {username}"}

@app.post("/playback/stop")
def stop_playback(movie_id: int, username: str):
    if username not in fake_users:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"Playback stopped for movie {movie_id} by {username}"}
