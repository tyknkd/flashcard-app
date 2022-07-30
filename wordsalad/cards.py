# !/usr/bin/python3

# Python script to create Blueprint to handle flashcard requests
# to `/decks/<deck_name>/`, `/decks/<deck_name>/add/`, `/decks/<deck_name>/<card_id>/edit/`
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/views/
# https://flask.palletsprojects.com/en/2.1.x/tutorial/blog/
# https://medevel.com/flask-tutorial-upload-csv-file-and-insert-rows-into-the-database/

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

# https://werkzeug.palletsprojects.com/en/2.1.x/utils/
from werkzeug.exceptions import abort

# Python library to handle operating system paths
import os

# Library to handle csv parsing
import csv 

# Require login function
from wordsalad.auth import login_required

# Database connection function
from wordsalad.db import get_db

# Deck functions
from wordsalad.decks import get_own_deck, get_deck

bp = Blueprint('cards', __name__, url_prefix='/decks/<int:deck_id>')

# Database Access Support Functions

def get_cards(deck_id: int) -> list:
    '''
    Fetch cards in deck by deck_id form data base
    :returns: list of dicts of cards (card_id, front, back, notes) (None if does not exist)
    '''
    # Connect to database
    db = get_db()
    
    # Get card data (None if does not exist)
    return db.execute('SELECT * FROM cards WHERE deck_id =?', (deck_id,)).fetchall()

def get_card(card_id: int) -> dict:
    '''
    Fetch single card in database by card_id (None if does not exist)
    :returns: dict of card_id, front, back, notes for card_id
    '''
    # Connect to database
    db = get_db ()
    
    # Get data for single card
    return db.execute('SELECT * FROM cards WHERE card_id=?', (card_id,)).fetchone()


def add_card(deck_id: int, front: str, back: str, notes: str) -> str:
    '''
    Insert row in 'cards' table of database
    :returns: Error message (None if successful)
    '''
    # Connect to database
    db = get_db()

    try:
        # Insert new row in database
        db.execute(
            'INSERT INTO cards (deck_id, front, back, notes)'
            ' VALUES (?, ?, ?, ?)',
            (deck_id, front, back, notes)
        )
        db.commit()

    # If error raised
    except db.Error as error:
       return f"Failed to add card {error}"

    else:
        return None

def parse_csv(deck_id: int, filepath) -> str:
    '''
    Insert rows from csv into 'cards' table of database
    :returns: Error message (None if successful)
    '''
    # Connect to database
    db = get_db()

    try:
        # Get data from CSV
        csv_rows = []
        with open (filepath, 'r', newline='') as csv_file:        
            rows = csv.reader(csv_file, delimiter=',')
            for row in rows:
                csv_rows.append(row)
        
        # Remove header row
        csv_rows.pop(0)

        # Insert rows into database
        for row in csv_rows: 
            db.execute(
                'INSERT INTO cards (deck_id, front, back, notes)'
                ' VALUES (?, ?, ?, ?)',
                (deck_id, row[0], row[1], row[2])
            )
        db.commit()

    # If error raised
    except db.Error as error:
       return f"Failed to add cards {error}"

    else:
        return None
    

def update(card_id: int, front: str, back: str, notes: str) -> str:
    '''
    Update card with card_id
    :returns: Error message (None if successful)
    '''
    # Connect to database
    db = get_db()
    
    try:
        # Update database
        db.execute(
            'UPDATE cards SET front = ?, back = ?, notes = ?'
            ' WHERE card_id = ?',
            (front, back, notes, card_id)
        )
        db.commit()

    # If error raised
    except db.Error as error:
       return f"Failed to update card {error}"

    else:
        return None

def remove(card_id: int) -> str:
    '''
    Remove card with card_id
    :returns: Error message (None if successful)
    '''
    # Connect to database
    db = get_db()
    
    try:
        # Delete deck 
        db.execute('DELETE FROM cards WHERE card_id = ?', (card_id,))
        db.commit()

    # If error raised
    except db.Error as error:
       return f"Failed to delete card {error}"

    else:
        return None    

def rows_to_list_of_dicts(rows) -> list:
    '''
    Convert sqlite3.Row object to Python list of dicts
    https://docs.python.org/3/library/sqlite3.html#sqlite3.Row
    https://stackoverflow.com/a/16523148
    :returns: dict of keys and values from sqlite3.Row object
    '''
    results = []
    for row in rows:
        results.append(dict(zip(row.keys(), row)))
    return results
    
# Associate `/decks/<deck_id>` with cards() function
@bp.route('/')
def cards(deck_id: int):
    '''
    Render HTML template displaying cards in deck
    '''
    # Get sqlite3.Row object of cards from deck
    cards_rows = get_cards(deck_id)

    # Convert to Python list
    cards = rows_to_list_of_dicts(cards_rows) 

    # Get dict of deck info for deck_id
    deck = get_deck(deck_id)
    
    return render_template('decks/cards/index.html', cards=cards, deck=deck)
    

@bp.route('/add/', methods=('GET', 'POST'))
@login_required
def add(deck_id: int):
    '''
    Add card to deck with deck_id
    '''
    # Get deck and check if user is owner
    deck = get_own_deck(deck_id)

    # Process form input
    if request.method == 'POST':
        front = request.form['front']
        back = request.form['back']
        notes = request.form['notes']

        error = None
        
        # Handle missing info
        if not front:
            error = 'Front of card is required'

        elif not back:
            error = 'Back of card is required'
 
        if error is None:
            # Add card to database
            error = add_card(deck_id, front, back, notes)
            
            if error is None:
                # Redirect to deck_id page
                return redirect(url_for('cards.cards', deck_id=deck_id))
        
        # Store error to retrieve when rendering template
        flash(error)
        
    return render_template('decks/cards/add.html', deck=deck)

# Associate '/decks/<deck_id>/upload/' with upload(deck_id)
@bp.route('/upload/', methods=('GET','POST'))
@login_required
def upload(deck_id: int):
    '''
    Add multiple cards from uploaded CSV
    '''
    # Process form input
    if request.method == 'POST':
        csv_file = request.form['file']

        error = None
        
        # Handle missing info
        if not csv_file:
            error = 'CSV file is required'

        if error is None:
            # Set file path
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], csv_file.filename)
            
            # Save file 
            uploaded_file.save(file_path)

            # Parse the file and add to database
            error = parse_csv(deck_id, file_path)
            
            if error is None:
                # Redirect to deck_id page
                return redirect(url_for('cards.cards', deck_id=deck_id))
        
        # Store error to retrieve when rendering template
        flash(error)
        
    return render_template('decks/cards/upload.html', deck=deck)

# Associate  '/decks/<deck_id>/<card_id>/edit/' with edit(card_id)
@bp.route('/<int:card_id>/edit/', methods=('GET', 'POST'))
@login_required
def edit(deck_id: int, card_id: int):
    '''
    Edit info of a card with card_id
    '''
    # Get card info
    card = get_card(card_id)
    
    # Get deck and check if user is owner
    deck = get_own_deck(deck_id)

    # Process form input
    if request.method == 'POST':
        front = request.form['front']
        back = request.form['back']
        notes = request.form['notes']

        error = None
        
        # Handle missing info
        if not front:
            error = 'Front of card is required'

        elif not back:
            error = 'Back of card is required'
 
        if error is None:
            # Update card in database
            error = update(card_id, front, back, notes)
            
            if error is None:
                # Redirect to deck_id page
                return redirect(url_for('cards.cards', deck_id=deck_id))
        
        # Store error to retrieve when rendering template
        flash(error)
        
    # Render page and pass card data
    return render_template('decks/cards/edit.html', deck=deck, card=card)
    
# Associate '/decks/<deck_id>/<card_id_/delete/' with delete()
@bp.route('/<int:card_id>/delete/', methods=('POST',))
@login_required
def delete(deck_id: int, card_id: int):
    '''
    Delete deck
    '''
    # Get card info
    card = get_card(card_id)
    
    # Get deck and check if user is owner
    deck = get_own_deck(deck_id)

    if card is not None:
        # Delete card 
        error = remove(card_id)

        if error is None:
            # Redirect to deck_id page
            return redirect(url_for('cards.cards', deck_id=deck_id))

    # Store error to retrieve when rendering template
    flash(error)

    # Render page and pass card data
    return render_template('decks/cards/edit.html', deck=deck, card=card)
