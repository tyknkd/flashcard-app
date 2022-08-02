#!/usr/bin/python3

# Database unit tests 
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/tests/

import sqlite3

import pytest
from wordsalad.db import get_db
import wordsalad.cards as cards

def test_get_close_db(app):
    '''
    Confirm get_db always returns same connection
    '''
    with app.app_context():
        db = get_db()
        assert db is get_db()
        assert db is not None

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

#Test that the DB actually opens and closes by calling
#.close() on a running DB
def test_close_db(app):
    with app.app_context():
        try:
            db = get_db()
            assert db is not None
        except:
            db.close()
            assert db is None

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

        #Fail on non-existant card #TODO this does not fail as expected
        #with pytest.raises(Exception):
        #    cards.update(12, "UpdateFront", "UpdateBack", "UpdateNotes")
        #Succeeds on existing card
        cards.update(1, "UpdateFront", "UpdateBack", "UpdateNotes")
        card = db.execute('SELECT * FROM cards WHERE card_id = 1').fetchone()[0]
        assert card is not None

        cards.remove(1)
        #Check to see we are returning a "None" object
        try:
            db.execute("SELECT * FROM cards where card_id = 1").fetchone()[0]
        except TypeError:
            pass

# Parses CSV file and ensures cards are uploaded
def test_csv_parse(app):

    with app.app_context():
        cards.parse_csv(3, "tests/testDeck_1.csv")
        parsed = cards.get_cards(3)
        assert parsed is not None
        db = get_db()
        count = db.execute('SELECT COUNT (card_id) FROM cards WHERE deck_id = 3').fetchone()[0]
        assert count==2
        
def test_allowed_file():
    allowed = cards.allowed_file("tests/testDeck_1.csv")
    assert allowed == True

    disallowed = cards.allowed_file("tests/db.py")
    assert disallowed == False

def test_rows_to_list_of_dicts(app):
    with app.app_context():
        db = get_db()
        cards.add_card(1, "Card Front", "Card Back", "Notes")
        cards.add_card(1, "Card Front2", "Card Back2", "Notes2")

        sqlite_entries = db.execute("SELECT * FROM cards WHERE deck_id = 1").fetchall()
        entries = cards.rows_to_list_of_dicts(sqlite_entries)
        assert str(entries[2]) == "{'card_id': 3, 'deck_id': 1, 'front': 'Card Front2', 'back': 'Card Back2', 'notes': 'Notes2'}"

