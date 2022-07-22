#!/usr/bin/python3

# Python script to create Blueprint to handle authentication requests to `/auth/register` 
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/views/

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

# https://werkzeug.palletsprojects.com/en/2.1.x/utils/
from werkzeug.security import check_password_hash, generate_password_hash

from wordsalad.db import get_db

# Create Blueprint
bp = Blueprint('auth', __name__, url_prefix='/auth')

# Database Access Support Functions
def add_user(name: str, email: str, username: str, password: str) -> str:
    '''
    Add new user to `users` table in database
    :return: Error message (None if successful) 
    '''
    
    # Connect to database
    db = get_db()

    try:
        # Insert new user data into `users` table of database
        db.execute(
            "INSERT INTO users (name, email, username, password) VALUES (?, ?, ?, ?)",
            (name, email, username, generate_password_hash(password)),
        )
        db.commit()
               
    # If user already exists
    except db.IntegrityError:
        return f"User {username} is already registered."

    else:
        return None

def get_user(username: str) -> dict:
    '''
    Get user details from `users` table in database
    :return: dict with user_id, name, email, username, password or None if no such username 
    '''
    
    # Connect to database
    db = get_db()

    # Query database for user and return row (None if not found)
    return db.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()
    
def get_user_from_id(user_id: int) -> dict:
    '''
    Get user details from `users` table in database
    :return: dict with user_id, name, email, username, password or None if no such user_id 
    '''
    
    # Connect to database
    db = get_db()

    # Query database for user and return row (None if not found)
    return db.execute(
            'SELECT * FROM users WHERE user_id= ?', (user_id,)
        ).fetchone()


# Wrapper to associate `/register` with `register` function
@bp.route('/register/', methods=('GET', 'POST'))
def register():
    '''
    Register new user
    '''
    # When registration form submitted
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        
        # Initialize error message
        error = None

        # Check that input fields are not empty
        if not name:
            error = 'Name is required'
        elif not email:
            error = 'Email is required.'
        elif not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            # Add user to database
            error = add_user(name, email, username, password)

            if error is None:     
                # Redirect to login page
                return redirect(url_for("auth.login"))

        # Store errors to retrieve when rendering template
        flash(error)

    # Unsuccessful, so render registration page again
    return render_template('auth/register.html')

# Associate `/login` with `login` function
@bp.route('/login/', methods=('GET', 'POST'))
def login():
    '''
    Verify user login
    '''
    # When login form submitted
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Initialize error message
        error = None
        
        user = get_user(username) 

        if user is None:
            error = 'Incorrect username.'
        
        # Check if hashed password matches    
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            # Store `user_id` in signed cookie sent to browser
            session['user_id'] = user['user_id']
            return redirect(url_for('index'))
        
        # Store errors to retrieve when rendering template
        flash(error)

    return render_template('auth/login.html')
    

# Wrapper to register function that runs before view function
@bp.before_app_request
def load_logged_in_user():
    '''
    Check if user id is stored in session
    If exists, get user's data from database
    '''
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        # Query database for user info
        g.user = get_user_from_id(user_id)


@bp.route('/logout/')
def logout():
    '''
    Log out user
    '''
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    '''
    Require login
    '''
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
