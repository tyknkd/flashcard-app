# !/usr/bin/python3

# Python script to create Blueprint to handle flashcard requests
# to `/decks/`, `/decks/<deck_name>`, `/decks/create/`, `/decks/edit/`,
# and `/decks/delete/`
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/views/
# https://flask.palletsprojects.com/en/2.1.x/tutorial/blog/

from crypt import methods
from webbrowser import get
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

# https://werkzeug.palletsprojects.com/en/2.1.x/utils/
from werkzeug.exceptions import abort

# Require login function
from wordsalad.auth import login_required

# Database connection function
from wordsalad.db import get_db

# Deck functions
from wordsalad.decks import get_own_deck, get_deck

bp = Blueprint('cards', __name__, url_prefix='/decks/<int:deck_id>')


# Get cards from database
def get_cards(deck_id: int):
    '''
    Fetch cards in deck by deck_id
    '''
    # Connect to database
    db = get_db()
    # Get card data (None if does not exist)
    return db.execute('SELECT * FROM cards WHERE deck_id =?', (deck_id,)).fetchall()

# 
@bp.route('/index', methods=('GET', 'POST'))
def cards(deck_id: int):
    '''
    Render HTML template with all cards in deck
    '''
    # Get cards from deck
    cards = get_cards (deck_id)
    # Get deck info from deck_id
    deck = get_deck(deck_id)

    return render_template('cards/card_index.html', cards=cards, deck=deck)
    


@bp.route('/add', methods=('GET', 'POST'))
@login_required
def add_card(deck_id: int):
    '''
    Add card to deck with deck_id
    '''
    # Get deck and check if user is owner
    deck = get_own_deck(deck_id)

    if request.method == 'POST':
        word = request.form['word']
        speech = request.form['speech']
        define = request.form['define']
        notes = request.form['notes']

        error = None
        # Handle missing info (part of speech and notes not required)
        if not word:
            error = 'Word is required'

        elif not speech:
            speech = ""

        elif not define:
            error = 'Definition is required'
        elif not notes:
            notes = ""
        definition = speech + " " + define
        # Update deck with new card
        if error is None:
            error = create_card(deck_id, word, definition, notes)

            if error is None:
                # Redirect to add card page
                return redirect(url_for('cards.add_card', deck_id=deck['deck_id']))

        # Store error to retrieve when rendering template
        flash(error)
    return render_template('cards/add.html', deck=deck)


# Create card in database
def create_card(deck_id: int, word: str, definition: str, notes: str):
    '''
    Insert row in 'cards' table of database
    :returns: Error message (None if successful)
    '''
    # connect to database
    db = get_db()

    try:
        # Insert new row in database
        db.execute(
            'INSERT INTO cards (deck_id, front, back, notes)'
            'VALUES(?, ?, ?, ?)', (deck_id, word, definition, notes)
        )

    # if error raised
    except db.Error as error:
        return f"Failed to add card {error}"

    db.commit()
    return None

