#!/usr/bin/python3

# User authentication unit tests 
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/tests/

import pytest
from flask import g, session
from wordsalad.db import get_db


def test_register(client, app):
    '''
    Test user registration
    '''
    # Confirm register view renders correctly 
    assert client.get('/auth/register').status_code == 200
    
    # Register valid user data 
    valid_user = {'name': 'Amos', 'email': 'amos@example.com', 'username': 'ajax', 'password': 'amazing'}
    response = client.post(
        '/auth/register', data=valid_user
    )
    
    # Confirm redirected to login page
    assert response.headers["Location"] == "/auth/login"

    # Confirm user now in database 
    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM users WHERE username = 'ajax'",
        ).fetchone() is not None
     
    # TO DO: Confirm all cols of user data

# Repeat test with different arguments
@pytest.mark.parametrize(('name','email','username', 'password', 'message'), (
    ('', '', '', '', b'Name is required.'),
    ('Bilbo', '', '', '', b'Email is required.'),
    ('Bilbo', 'bilbo@example.com', '', b'Username is required.'),
    ('Bilbo', 'bilbo@example.com', 'bilbao', '', b'Password is required.'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, name, email, username, password, message):
    '''
    Test form validation
    '''
    response = client.post(
        '/auth/register',
        data={'name': name, 'email': email, 'username': username, 'password': password}
    )
    assert message in response.data
