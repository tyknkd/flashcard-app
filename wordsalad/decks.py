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

@bp.route('/decks/')
def decks():
    '''
    Display available decks
    '''
    # Get deck names, descriptions, public status from database
    db = get_db()
    decks = db.execute(
        'SELECT name, description, public FROM decks'
    ).fetchall()
    return render_template('decks/index.html', decks=decks)


@bp.route('/decks/create', methods=('GET', 'POST'))
@login_required
def create():
    '''
    Create new flashcard deck
    '''
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        description = request.form['description']
        public = request.form['public']
        error = None

        # Handle missing info
        if not name:
            error = 'Deck name is required.'
            
        elif not category:
            error = 'Category is required.'
            
        elif not description:
            error = 'Description is required.'

        elif not public:
            error = 'Public/private is required.'
        
        if error is not None:
            flash(error)
        else:
            # Add deck to database
            db = get_db()
            db.execute(
                'INSERT INTO decks (name, category, owner_id, public, description)'
                ' VALUES (?, ?, ?, ?, ?)',
                (name, category, g.user['user_id'], public, description)
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
        'SELECT deck_id, name, category, owner_id, public, description'
        ' FROM decks WHERE deck_id = ?',
        (deck_id,)
    ).fetchone()

    if post is None:
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
        name = request.form['name']
        category = request.form['category']
        description = request.form['description']
        public = request.form['public']
        error = None

        # Handle missing info
        if not name:
            error = 'Deck name is required.'
            
        elif not category:
            error = 'Category is required.'
            
        elif not description:
            error = 'Description is required.'

        elif not public:
            error = 'Public/private is required.'

        if error is not None:
            flash(error)
        else:
            # Update database
            db = get_db()
            db.execute(
                'UPDATE decks SET name = ?, category = ?, description = ?, public = ?'
                ' WHERE deck_id = ?',
                (name, category, description, public, deck_id)
            )
            db.commit()
            return redirect(url_for('decks.index'))

    return render_template('decks/edit.html', deck=deck)
