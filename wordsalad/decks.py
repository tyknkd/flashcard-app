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
def get_decks() -> dict:
    '''
    Gets data for all decks in `decks` table of database
    :return: dict of deck_id, owner_id, title, category, description, public
    '''
    # Connect to database
    db = get_db()

    # Return dict of all decks rows
    return db.execute('SELECT * FROM decks').fetchall()


# Wrapper to associate `/decks/` route with `decks()` function
@bp.route('/decks/')
def decks():
    '''
    Render HTML template with all available decks
    '''
    # Get dict of all cols of all rows in decks table of database
    decks = get_decks()

    return render_template('decks/index.html', decks=decks)


@bp.route('/decks/create', methods=('GET', 'POST'))
@login_required
def create():
    '''
    Create new flashcard deck
    '''
    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        description = request.form['description']
        public = request.form['public']
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
        
        if error is not None:
            flash(error)
        else:
            # Add deck to database
            db = get_db()
            db.execute(
                'INSERT INTO decks (owner_id, title, category, description, public)'
                ' VALUES (?, ?, ?, ?, ?)',
                (g.user['user_id'], title, category, description, public)
            )
            db.commit()
            return redirect(url_for('decks.index'))

    return render_template('decks/create.html')
    
def get_deck(deck_id, check_owner=True):
    '''
    Fetch deck by deck_id
    :check_owner=True: Abort if user is not owner
    '''
    deck = get_db().execute(
        'SELECT deck_id, owner_id, title, category, description, public'
        ' FROM decks WHERE deck_id = ?',
        (deck_id,)
    ).fetchone()

    if deck is None:
        abort(404, f"Deck id {deck_id} doesn't exist.")

    # Check that user is owner of deck
    if check_owner and deck['owner_id'] != g.user['user_id']:
        abort(403)
    
    return deck

@bp.route('/<int:deck_id>/edit', methods=('GET', 'POST'))
@login_required
def edit(deck_id):
    '''
    Edit info of a deck with deck_id
    '''
    deck = get_deck(deck_id)

    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        description = request.form['description']
        public = request.form['public']
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

        if error is not None:
            flash(error)
        else:
            # Update database
            db = get_db()
            db.execute(
                'UPDATE decks SET title = ?, category = ?, description = ?, public = ?'
                ' WHERE deck_id = ?',
                (deck_id, title, category, description, public)
            )
            db.commit()
            return redirect(url_for('decks.index'))

    return render_template('decks/edit.html', deck=deck)
    
@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(deck_id):
    '''
    Delete deck
    '''
    get_deck(deck_id)
    db = get_db()
    db.execute('DELETE FROM decks WHERE deck_id = ?', (deck_id,))
    db.commit()
    return redirect(url_for('decks.index'))  
