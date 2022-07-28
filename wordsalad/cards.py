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

# Get single card in deck from database
def get_card(card_id: int):
    '''
    Fetch single card in database by card_id
    '''
    # Connect to database
    db = get_db ()
    # Get data for single card
    return db.execute('SELECT * FROM cards WHERE card_id=?', (card_id,)).fetchone()

# Get first card in deck
def get_first_card(deck_id: int):
    '''
    Get first card in deck from database by deck_id
    '''
    # Get cards in deck
    cards = get_cards(deck_id)
    #return first card
    first = cards[0]
    return first

# Display all cards in deck
@bp.route('/index', methods=('GET', 'POST'))
def cards(deck_id: int):
    '''
    Render HTML template with all cards in deck
    '''
    # Get cards from deck
    cards = get_cards (deck_id)

    # Get deck info from deck_id
    deck = get_deck(deck_id)
    if not cards:
        return render_template('cards/card_index.html', deck=deck)
    # Get first card from deck
    first = get_first_card(deck_id)

    return render_template('cards/card_index.html', cards=cards, deck=deck, first=first)
    


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
            
            return redirect(url_for('cards.cards', deck_id=deck['deck_id']))
        else:
            error = "Did not add to table"
        
            return redirect(url_for('decks/decks.html'))
        # Store error to retrieve when rendering template
        flash(error)
    return render_template('cards/add.html', deck=deck)


# Create card in database
def create_card(deck_id: int, word: str, definition: str, notes: str):
    '''
    Insert row in 'cards' table of database
    :returns: Error message (None if successful)
    '''
    # Connect to database
    db = get_db()

    # db.execute(
    #     'INSERT INTO cards (deck_id, front, back, notes)'
    #     'VALUES (?, ?, ?, ?)',
    #     (deck_id, word, definition, notes)
    # )
    # db.commit()
    # render_template('decks/create.html')
    # return None

    
    try:
        # Insert new row in database
        db.execute(
            'INSERT INTO cards (deck_id, front, back, notes)'
            ' VALUES (?, ?, ?, ?)',
            (deck_id, word, definition, notes)
        )
        db.commit()

    # If error raised
    except db.Error as error:
       return f"Failed to add deck {error}"

    else:
        return None

# View single card
@bp.route ('/view/<int:card_id>', methods=('GET', 'POST'))
def view_card (deck_id: int, card_id: int):
    '''
    View one card at a time in deck
    '''
    # Get info from database
    deck = get_deck(deck_id)
    first = get_first_card(deck_id)
    cards = get_cards(deck_id)
    card = get_card (card_id)
    # If there is no next card
    if not card:
        prev_card = card_id - 1
        new_card = get_card(prev_card)
        cards = get_cards(deck_id)
        return render_template('cards/card_index.html', cards=cards, deck=deck, first=first)

    # Check card belongs to deck
    if deck_id != card['deck_id']:
        return render_template('cards/card_index.html', cards=cards, deck=deck, first=first)

    return  render_template('cards/view.html', deck = deck, card=card)

