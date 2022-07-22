#!/usr/bin/python3

# Python script to create Blueprint to handle homeand about page requests 
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
from wordsalad.decks import get_decks

bp = Blueprint('home', __name__)

# Wrapper to associate '/' with index()
@bp.route('/')
def index():
    '''
    Render home page 
    '''
    # Get info for all decks from database
    decks = get_decks()
    return render_template('index.html', decks=decks)

@bp.route('/about')
def about():
    '''
    Render about page 
    '''
    return render_template('about.html')
