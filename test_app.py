import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Test the main endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data

def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}
