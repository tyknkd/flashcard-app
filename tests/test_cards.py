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


def test_add(client, auth, app):
    auth.login()

    assert client.get('/decks/1/add/').status_code == 200
    client.post(
        '/decks/1/add/',
        data={
            'front': 'Card1 Front',
            'back': 'Card1 Back',
            'notes': 'Notes Card1'
        }
    )

    #confirm card is there
    with app.app_context():
        db = get_db()
        sqlite_card = db.execute('SELECT * FROM cards WHERE front = "Card1 Front"').fetchall()
        card = cards.rows_to_list_of_dicts(sqlite_card)
        assert str(card) == "[{'card_id': 2, 'deck_id': 1, 'front': 'Card1 Front', 'back': 'Card1 Back', 'notes': 'Notes Card1'}]"


def test_edit(client, auth, app):
    auth.login()

    assert client.get('decks/1/1/edit/').status_code == 200
    client.post(
        'decks/1/1/edit/',
        data = {
            'front': 'CARD EDIT',
            'back': 'CARD EDIT',
            'notes': 'CARD EDIT'
        }
    )

    #confirm card is there
    with app.app_context():
        db = get_db()
        sqlite_card = db.execute('SELECT * FROM cards WHERE front = "CARD EDIT"').fetchall()
        card = cards.rows_to_list_of_dicts(sqlite_card)
        assert str(card) == "[{'card_id': 1, 'deck_id': 1, 'front': 'CARD EDIT', 'back': 'CARD EDIT', 'notes': 'CARD EDIT'}]"


def test_delete(client, auth, app):
    auth.login()

    #creating a deck
    client.post(
        '/decks/create/', 
        data={
            'title': 'New Deck', 
            'category': 'new_category', 
            'description': 'New deck description.', 
            'public': 'TRUE'
        }
    )

    #creating a card
    client.post(
        '/decks/2/add/',
        data={
            'front': 'Card1 Front',
            'back': 'Card1 Back',
            'notes': 'Notes Card1'
        }
    )

    client.post(
        'decks/2/2/delete/',
        data = {}
    )
    client.post(
        'decks/1/1/delete/',
        data = {}
    )

    #confirm card is gone
    with app.app_context():
        db = get_db()
        sqlite_card = db.execute('SELECT * FROM cards').fetchall()
        card = cards.rows_to_list_of_dicts(sqlite_card)
        assert card == []