import pytest
import json
from app.main import app


@pytest.fixture
def client():
    """
    Create a test client for the Flask application
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def runner():
    """
    Create a test runner for CLI commands
    """
    return app.test_cli_runner()


def test_home_endpoint(client):
    """
    Test the home endpoint returns correct information
    """
    response = client.get('/')
    assert response.status_code == 200

    data = response.get_json()
    assert data['message'] == 'DevOps Flask API'
    assert data['version'] == '1.0.0'
    assert data['status'] == 'running'
    assert 'environment' in data


def test_health_endpoint(client):
    """
    Test the health endpoint returns healthy status
    """
    response = client.get('/health')
    assert response.status_code == 200

    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'timestamp' in data


def test_users_endpoint(client):
    """
    Test the users endpoint returns user data
    """
    response = client.get('/api/users')
    assert response.status_code == 200

    data = response.get_json()
    assert 'users' in data
    assert 'count' in data
    assert data['count'] == 3
    assert len(data['users']) == 3

    # Test first user structure
    first_user = data['users'][0]
    assert 'id' in first_user
    assert 'name' in first_user
    assert 'role' in first_user
    assert 'department' in first_user


def test_status_endpoint(client):
    """
    Test the status endpoint returns system information
    """
    response = client.get('/api/status')
    assert response.status_code == 200

    data = response.get_json()
    assert data['api_status'] == 'operational'
    assert 'environment' in data


def test_nonexistent_endpoint(client):
    """
    Test that nonexistent endpoints return 404
    """
    response = client.get('/nonexistent')
    assert response.status_code == 404


def test_content_type_is_json(client):
    """
    Test that all endpoints return JSON content type
    """
    endpoints = ['/', '/health', '/api/users', '/api/status']

    for endpoint in endpoints:
        response = client.get(endpoint)
        assert response.content_type == 'application/json'