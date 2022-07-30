#!/usr/bin/python3

# Cards pages unit tests 
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/tests/

import pytest
from wordsalad.db import get_db


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
