
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


# Repeat following test with different arguments
@pytest.mark.parametrize('path', (
    '/create',
    '/1/edit',
    '/1/delete',
))
def test_login_required(client, path):
    '''
    Confirm login required
    '''
    response = client.post(path)
    assert response.headers["Location"] == "/auth/login"


def test_owner_required(app, client, auth):
    # Change the deck owner to another user
    with app.app_context():
        db = get_db()
        db.execute('UPDATE decks SET owner_id = 2 WHERE deck_id = 1')
        db.commit()

    # Login as test user (user_id=1)
    auth.login()
    
    # Confirm current user cannot modify other user's deck
    assert client.post('/1/edit').status_code == 403
    assert client.post('/1/delete').status_code == 403
    
    # Confirm current user does not see edit link
    assert b'href="/1/edit"' not in client.get('/decks').data

# Repeat following test with different arguments
@pytest.mark.parametrize('path', (
    '/2/edit',
    '/2/delete',
))
def test_exists_required(client, auth, path):
    '''
    Confirm nonexistent deck cannot be edited
    '''
    auth.login()
    assert client.post(path).status_code == 404
