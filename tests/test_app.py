"""Unit tests for the Flask application."""
import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client

def test_hello_world_endpoint(client):
    """Test the main '/' endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello World"}

def test_health_check_endpoint(client):
    """Test the '/health' endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}