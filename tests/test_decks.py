
#!/usr/bin/python3

# Decks pages unit tests 
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
    '/decks/create',
    '/decks/1/edit',
    '/decks/1/delete',
))
def test_login_required(client, path):
    '''
    Confirm login required
    '''
    # Confirm redirected to login page 
    # when accessing page requiring login
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
    '/decks/2/edit',
    '/decks/2/delete',
))
def test_exists_required(client, auth, path):
    '''
    Confirm nonexistent deck cannot be edited
    '''
    auth.login()
    assert client.post(path).status_code == 404

def test_create(client, auth, app):
    '''
    Test deck creation
    '''
    auth.login()

    # Confirm /decks/create/ loads
    assert client.get('/decks/create').status_code == 200
    
    # Add new deck
    client.post(
        '/decks/create', 
        data={
            'name': 'New Deck', 
            'category': 'new_category', 
            'public': 'TRUE', 
            'description': 'New deck description.'
        }
    )

    # Confirm two decks now exist in database
    with app.app_context():
        db = get_db()
        
        ### WHY IS [0] NEEDED IN THE FOLLOWING CODE? ###
        
        count = db.execute('SELECT COUNT(deck_id) FROM decks').fetchone()[0] 
        assert count == 2

def test_edit(client, auth, app):
    '''
    Test deck editing
    '''
    auth.login()

    # Confirm /decks/1/edit/ loads
    assert client.get('/decks/1/edit').status_code == 200
    
    # Edit deck
    client.post(
        '/decks/1/edit', 
        data={
            'name': 'Updated Test Title', 
            'category': 'updated_category', 
            'public': 'TRUE', 
            'description': 'Updated test deck description.'
        }
    )

    # Confirm deck updated
    with app.app_context():
        db = get_db()
        deck = db.execute('SELECT * FROM decks WHERE deck_id = 1').fetchone()
        assert deck['name'] == 'Updated Test Title'
        assert deck['category'] == 'updated_category'
        
        ### SHOULD 'TRUE' BE REPLACED WITH 1 IN FOLLOWING LINE? ###
        
        assert deck['public'] == 'TRUE'  
        
        assert deck['description'] == 'Updated test deck description'
        
        
   ## ALSO TEST THAT OTHER FIELDS REMAIN SAME WHEN ONLY ONE FIELD IS EDITED? ##

# Repeat following test with different arguments
@pytest.mark.parametrize('path', (
    '/decks/create',
    '/decks/1/edit',
))
def test_create_edit_validate(client, auth, path):
    '''
    Confirm valid entry required
    '''
    auth.login()
    
    # Attempt to enter blank fields
    response = client.post(
        path, data={'name': '', 'category': '', 'public': '', 'description': ''}
    )
    assert b'Deck name is required.' in response.data
    
    ## TO DO: CHECK THAT ERROR MESSAGES FOR OTHER FIELDS DISPLAY WHEN PRECEDING FIELDS VALID ##
    
  
def test_delete(client, auth, app):
    '''
    Test deck deletion
    '''
    auth.login()
    
    # Delete Deck 1
    response = client.post('/decks/1/delete')
    
    # Confirm redirect to decks page
    assert response.headers["Location"] == "/decks"

    # Confirm deck does not exist
    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM decks WHERE deck_id = 1').fetchone()
        assert post is None
