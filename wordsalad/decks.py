#!/usr/bin/python3

# Python script to create Blueprint to handle flashcard deck requests 
# to `/decks/`, `/decks/<deck_name>`, and `/decks/edit/*` 
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
    db = get_db()
    decks = db.execute(
        'SELECT name, description, public FROM decks'
    ).fetchall()
    return render_template('decks/index.html', decks=decks)
