# conftest.py
import pytest
from fastapi.testclient import TestClient
from api.main import app


@pytest.fixture
def client():
    """
    Fixture for FastAPI test client.
    Provides a reusable HTTP client for all tests.
    """
    with TestClient(app) as c:
        yield c
