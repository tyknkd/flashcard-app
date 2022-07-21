#!/usr/bin/python3

# Python script to create Blueprint to handle home/main and about page requests 
# to `/` and `/about/` 
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

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    '''
    Home/main page route
    '''
    # Get deck names, descriptions, public status from database
    db = get_db()
    decks = db.execute(
        'SELECT name, description, public FROM decks'
    ).fetchall()
    return render_template('index.html', post=decks)
