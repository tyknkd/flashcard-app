#!/usr/bin/python3

# Cards pages unit tests 
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/tests/

import pytest
from wordsalad.db import get_db
import wordsalad.cards as cards

def test_cards(client, auth):
    '''
    Test cards page
    '''
    # Get response to deck view w/o logging in
    response = client.get('/decks/1/')
    
    # Confirm "Log In" and "Register" on page
    assert b"Log In" in response.data
    assert b"Register" in response.data

    # Login and get response to decks view
    auth.login()
    response = client.get('/decks/1/')
    
    # Confirm "Log Out" on page
    assert b'Log Out' in response.data
    
    # Confirm card front from tests/data.sql displayed on page
    assert b'test card front' in response.data

# Repeat following test with different arguments
@pytest.mark.parametrize('path', (
    '/decks/1/add/',
    '/decks/1/1/edit/',
))
def test_login_required(client, path):
    '''
    Confirm login required
    '''
    # Confirm redirected to login page 
    # when accessing page requiring login
    response = client.post(path)
    assert response.headers["Location"] == "/auth/login/"

# Repeat following test with different arguments
@pytest.mark.parametrize('path', (
    '/decks/cards/edit',
))
def test_exists_required(client, auth, path):
    '''
    Confirm nonexistent deck cannot be edited
    '''
    auth.login()
    assert client.post(path).status_code == 404

# Repeat following test with different arguments
@pytest.mark.parametrize('path', (
    'decks/cards/index'
))
def test_cards(client, auth, path):
