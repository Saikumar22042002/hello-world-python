"""
Unit tests for the hello-world-python Flask application.
"""
import pytest
from app import app as flask_app

@pytest.fixture(scope='module')
def app():
    """Create and configure a new app instance for each test module."""
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app

@pytest.fixture(scope='module')
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_index_endpoint(client):
    """Test the main '/' endpoint for correct status code and message."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello World"}

def test_health_endpoint(client):
    """Test the '/health' endpoint for correct status code and message."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
