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


def test_card_functions(app):

    # Add a card and confirm it exist in database
    with app.app_context():
        db = get_db()
        cards.add_card(1, "Card Front", "Card Back", "Notes")
        
        count = db.execute('SELECT COUNT(card_id) FROM cards').fetchone()[0] 
        assert count == 2

        # Querying DB for Cards
        card_return = cards.get_cards(1)
        assert card_return is not None
        assert len(card_return) == 2

        single_return = cards.get_card(1)
        assert single_return is not None

        


        