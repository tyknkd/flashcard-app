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

# Repeat following test with different arguments
@pytest.mark.parametrize(('name','email','username', 'password', 'message'), (
    ('', '', '', '', b'Name is required.'),
    ('Bilbo', '', '', '', b'Email is required.'),
    ('Bilbo', 'bilbo@shire.com', '', '', b'Username is required.'),
    ('Bilbo', 'bilbo@shire.com', 'baggins', '', b'Password is required.'),
    ('test', 'test@test.com', 'test', 'test', b'already registered'),
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
    
def test_login(client, auth):
    '''
    Test login view
    '''
    # Confirm login view renders correctly 
    assert client.get('/auth/login').status_code == 200
    
    # Confirm redirect to home page after valid login
    response = auth.login()
    assert response.headers["Location"] == "/"

    # Confirm session has correct user_id & username after login
    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'

# Repeat following test with different arguments
@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Incorrect username.'),
    ('ajax', 'test', b'Incorrect username.'),
    ('test', '', b'Incorrect password.'),
    ('test', 'amazing', b'Incorrect password.'),
))
def test_login_validate_input(auth, username, password, message):
    '''
    Confirm error message returned for invalid username/password
    '''
    response = auth.login(username, password)
    assert message in response.data

def test_logout(client, auth):
    '''
    Test logout
    '''
    # Valid login
    auth.login()

    # Confirm user_id not in session after logout
    with client:
        auth.logout()
        assert 'user_id' not in session
