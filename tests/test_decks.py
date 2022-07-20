
#!/usr/bin/python3

# Decks page unit tests 
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/tests/

import pytest
from wordsalad.db import get_db

def test_decks(client, auth):
    '''
    Test decks page
    '''
    # Get response to decks view w/o logging in
    response = client.get('/decks')
    
    # Confirm "Log In" and "Register" on page
    assert b"Log In" in response.data
    assert b"Register" in response.data

    # Login and get response to decks view
    auth.login()
    response = client.get('/decks')
    
    # Confirm "Log Out" on page
    assert b'Log Out' in response.data
    
    # Confirm deck name and description from tests/data.sql displayed on page
    assert b'Test Title' in response.data
    assert b'This is a test deck description.' in response.data
