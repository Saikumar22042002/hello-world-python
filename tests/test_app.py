import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test the main '/' endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello World"}

def test_health(client):
    """Test the '/health' endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
