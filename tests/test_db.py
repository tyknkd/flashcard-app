#!/usr/bin/python3

# Database unit tests 
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/tests/

import sqlite3

import pytest
from wordsalad.db import get_db
import wordsalad.decks, wordsalad.auth #, wordsalad.cards # <- import once implemented

def test_get_close_db(app):
    '''
    Confirm get_db always returns same connection
    '''
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)
    
def test_init_db_command(runner, monkeypatch):
    '''
    Confirm init-db calls init_db
    '''
    class Recorder(object):
        called = False

    def fake_init_db():
        '''
        Fake init_db that records if called
        '''
        Recorder.called = True

    # Replace init_db with fake_init_db
    monkeypatch.setattr('wordsalad.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called    


def test_add_user(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()
    
    #Add user
    #Add user that already exists
    #Add invalid user
    return

def test_return_user():
    #Request valid user
    #Request user that does not exist
    return

def test_add_deck():
    return

def test_return_deck():
    return

def test_add_card():
    return

def test_return_card():
    return
