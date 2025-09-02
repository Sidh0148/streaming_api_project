# 🎬 Streaming API Test Suite

This project is a **mock streaming service API** built with [FastAPI](https://fastapi.tiangolo.com/), 
with a **pytest test suite** to validate endpoints.

---

## 🚀 Features
- **Authentication**
  - Login with username/password
- **Movies**
  - Get all movies
  - Filter by genre
  - Get single movie by ID
- **Watchlist**
  - Add movies to user watchlist
  - Retrieve user watchlist
- **Playback**
  - Start/stop playback for movies

---

## 🧪 Test Coverage
- ✅ Successful & failed login
- ✅ Movie list + schema validation
- ✅ Watchlist (valid & invalid users)
- ✅ Playback start/stop (valid & invalid users)

---

## 📂 Project Structure
streaming_api_project/
│── api/
│ └── main.py # FastAPI application
│
│── tests/
│ ├── test_auth.py # Authentication tests
│ ├── test_movies.py # Movies endpoint tests
│ ├── test_watchlist.py# Watchlist tests
│ └── test_playback.py # Playback tests
│
├── conftest.py # Pytest client fixture
├── pytest.ini # Pytest configuration
└── requirements.txt # Dependencies

Copy code

---

## ⚡ Setup & Run

### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Run FastAPI (optional, to try endpoints manually)
bash
Copy code
uvicorn api.main:app --reload
Visit API docs: http://127.0.0.1:8000/docs

4. Run tests
bash
Copy code
pytest
📌 Example Test Run
arduino
Copy code
tests/test_auth.py::test_login_success PASSED
tests/test_auth.py::test_login_failure PASSED
tests/test_movies.py::test_get_movies PASSED
tests/test_movies.py::test_get_movies_schema PASSED
tests/test_movies.py::test_get_movie_not_found PASSED
tests/test_watchlist.py::test_add_to_watchlist PASSED
tests/test_watchlist.py::test_get_watchlist PASSED
tests/test_watchlist.py::test_add_to_watchlist_invalid_user PASSED
tests/test_playback.py::test_start_playback PASSED
tests/test_playback.py::test_stop_playback PASSED
tests/test_playback.py::test_start_playback_invalid_user PASSED

================== 11 passed in 0.25s ==================