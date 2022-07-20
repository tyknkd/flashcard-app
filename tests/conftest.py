#!/usr/bin/python3

# Unit test configuration script to be run for each unit test 
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/tests/

import os
import tempfile

import pytest
from wordsalad import create_app
from wordsalad.db import get_db, init_db

# Read SQL test data
with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')

@pytest.fixture
def app():
    '''
    App generator
    '''
    # Create temporary file
    db_fd, db_path = tempfile.mkstemp()

    # Set app to test mode
    # Override default database path
    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    # Initialize database
    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    # Return app to caller without terminating this function
    yield app

    # Close and remove temporary file
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    '''
    Client to handle test requests without server
    '''
    return app.test_client()

@pytest.fixture
def runner(app):
    '''
    Runner to call Click commands within app
    '''
    return app.test_cli_runner()

# Class to handle user authentication procedures
class AuthActions(object):
    def __init__(self, client):
        self._client = client
    
    # Login as test user inserted from data.sql
    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')

@pytest.fixture
def auth(client):
    return AuthActions(client)
