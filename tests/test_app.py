import pytest
from app import app as flask_app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    with flask_app.test_client() as test_client:
        yield test_client

def test_home_endpoint(client):
    """Test the main '/' endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data

def test_health_check_endpoint(client):
    """Test the '/health' endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
