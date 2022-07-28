#!/usr/bin/python3

# Cards pages unit tests 
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/tests/

import pytest
from wordsalad.db import get_db
# Deck functions
from wordsalad.decks import get_own_deck, get_deck

def test_cards(client, auth):
    '''
    Test cards page
    '''
