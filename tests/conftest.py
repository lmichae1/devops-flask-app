import pytest
import sys
import os

# Add the parent directory to the path so we can import the app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(scope='session')
def app():
    """
    Create application for the tests
    """
    from app.main import app
    app.config['TESTING'] = True
    return app