#!/usr/bin/python3

# Python script to create Blueprint to handle flashcard deck requests 
# to `/decks/`, `/decks/<deck_name>`, `/decks/create/`, `/decks/edit/`,
# and `/decks/delete/`
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/views/
# https://flask.palletsprojects.com/en/2.1.x/tutorial/blog/

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

# https://werkzeug.palletsprojects.com/en/2.1.x/utils/
from werkzeug.exceptions import abort

# Require login function
from wordsalad.auth import login_required

# Database connection function
from wordsalad.db import get_db

bp = Blueprint('decks', __name__)

# Database Access Support Functions
def get_decks(owner_id) -> dict:
    '''
    Gets data for all public and owned decks for owner_id from `decks` table of database
    If owner_id = None, only public decks are returned
    :returns: dict of deck_id, owner_id, title, category, description, public
    '''
    # Connect to database
    db = get_db()

    if owner_id is None:
        # Return dict of only public decks 
        return db.execute(
                'SELECT * FROM decks WHERE public = ?', ('TRUE',)).fetchall()
    else: 
        # Return dict of public decks and decks belonging to owner_id
        return db.execute(
                'SELECT * FROM decks WHERE public = ? OR owner_id = ?', 
                ('TRUE', owner_id)).fetchall()

def get_deck(deck_id: int) -> dict:
    '''
    Fetch deck by deck_id
    :returns: dict of data for deck_id (None if does not exist)
    '''
    # Connect to database
    db = get_db()

    # Get deck data (None if does not exist)
    return db.execute('SELECT * FROM decks WHERE deck_id = ?', (deck_id,)).fetchone()

def get_own_deck(deck_id: int, check_owner=True) -> dict:
    '''
    Fetch deck by deck_id
    :param deck_id: deck_id of desired deck
    :param check_owner=True: Abort if user is not owner
    :returns: dict of deck data for deck_id (None if does not exist)
    '''
    # Get dict of deck data
    deck = get_deck(deck_id) 

    if deck is None:
        abort(404, f"Deck id {deck_id} doesn't exist.")

    # Check that user is owner of deck
    if check_owner and deck['owner_id'] != g.user['user_id']:
        abort(403)
    
    return deck

def add_deck(owner_id: int, title: str, category: str, description: str, public: bool) -> str:
    '''
    Insert row in `decks` table of database
    :returns: Error message (None if successful)
    '''
    # Connect to database
    db = get_db()
    
    try:
        # Insert new row in database
        db.execute(
            'INSERT INTO decks (owner_id, title, category, description, public)'
            ' VALUES (?, ?, ?, ?, ?)',
            (owner_id, title, category, description, public)
        )
        db.commit()

    # If error raised
    except db.Error as error:
       return f"Failed to add deck {error}"

    else:
        return None

def update(deck_id: int, title: str, category: str, description: str, public: bool) -> str:
    '''
    Update deck with deck_id
    :returns: Error message (None if successful)
    '''
    # Connect to database
    db = get_db()
    
    try:
        # Update database
        db.execute(
            'UPDATE decks SET title = ?, category = ?, description = ?, public = ?'
            ' WHERE deck_id = ?',
            (title, category, description, public, deck_id)
        )
        db.commit()

    # If error raised
    except db.Error as error:
       return f"Failed to update deck {error}"

    else:
        return None

def remove(deck_id: int) -> str:
    '''
    Remove deck with deck_id
    :returns: Error message (None if successful)
    '''
    # Connect to database
    db = get_db()
    
    try:
        # Delete deck 
        db.execute('DELETE FROM decks WHERE deck_id = ?', (deck_id,))
        db.commit()

    # If error raised
    except db.Error as error:
       return f"Failed to delete deck {error}"

    else:
        return None


# Wrapper to associate `/decks` route with `decks()` function
@bp.route('/decks/')
def decks():
    '''
    Render HTML template with all decks available to user
    '''
    # If user not logged in
    if g.user is None:
        # Get only public decks
        decks = get_decks(None)
    else:
        # Get all public decks and decks belonging to user
        decks = get_decks(g.user['user_id'])

    return render_template('decks/index.html', decks=decks)


@bp.route('/decks/create/', methods=('GET', 'POST'))
@login_required
def create():
    '''
    Create new flashcard deck
    '''
    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        description = request.form['description']
        public_check = request.form.get('public')
        if public_check == None:
            public = 'FALSE'
        else:
            public = 'TRUE'
        error = None

        error = None

        # Handle missing info
        if not title:
            error = 'Title is required.'

        elif not category:
            error = 'Category is required.'

        elif not description:
            error = 'Description is required.'

        elif not public:
            error = 'Public is required.'

        if error is None:
            # Add deck to database
            error = add_deck(g.user['user_id'], title, category, description, public)

            if error is None:
                # Redirect to decks page
                return redirect(url_for('decks.index'))

        # Store error to retrieve when rendering template
        flash(error)

    return render_template('decks/create.html')
    
# Associate  '/decks/<deck_id>/edit/' with edit(deck_id)
@bp.route('/decks/<int:deck_id>/edit/', methods=('GET', 'POST'))
@login_required
def edit(deck_id: int):
    '''
    Edit info of a deck with deck_id
    '''
    # Get deck and check if user is owner
    deck = get_own_deck(deck_id)

    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        description = request.form['description']
        public_check = request.form.get('public')
        if public_check == None:
            public = 'FALSE'
        else:
            public = 'TRUE'
        error = None

        # Handle missing info
        if not title:
            error = 'Title is required.'

        elif not category:
            error = 'Category is required.'

        elif not description:
            error = 'Description is required.'

        elif not public:
            error = 'Public is required.'

        if error is None:
            # Update deck
            error = update(deck_id, title, category, description, public)

            if error is None:
                # Redirect to decks page
                return redirect(url_for('decks.index'))

        # Store error to retrieve when rendering template
        flash(error)

    # Render page and pass deck data
    return render_template('decks/edit.html', deck=deck)
    
# Associate '/decks/<deck_id>/delete/' with delete()
@bp.route('/decks/<int:deck_id>/delete/', methods=('POST',))
@login_required
def delete(deck_id):
    '''
    Delete deck
    '''
    # Get deck and check if user is owner
    deck = get_own_deck(deck_id)

    if deck is not None:
        # Delete deck 
        error = remove(deck_id)

        if error is None:
            # Redirect to decks page
            return redirect(url_for('decks.index'))

    # Store error to retrieve when rendering template
    flash(error)

    # Render page and pass deck data
    return render_template('decks/edit.html', deck=deck)
