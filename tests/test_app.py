"""
Unit tests for the Flask application.
Ensures that all endpoints are functioning correctly.
"""
import pytest
from app import app as flask_app

@pytest.fixture(name="client")
def client_fixture():
    """Create and configure a new app instance for each test."""
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as test_client:
        yield test_client

def test_index_endpoint(client):
    """Test the main '/' endpoint for the correct message and status code."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello World"}

def test_health_check_endpoint(client):
    """Test the '/health' endpoint for a healthy status and 200 OK."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
