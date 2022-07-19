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

# Associate `/register` with `register` function
@bp.route('/register', methods=('GET', 'POST'))
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
        
        # Connect to database
        db = get_db()
        
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
            try:
                # Insert new user data into `users` table of database
                db.execute(
                    "INSERT INTO users (name, username, email, password) VALUES (?, ?, ?, ?)",
                    (name, username, email, generate_password_hash(password)),
                )
                db.commit()
                
            # If user already exists
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                # Redirect to login page
                return redirect(url_for("auth.login"))

        # Store errors to retrieve when rendering template
        flash(error)

    return render_template('auth/register.html')

# Associate `/login` with `login` function
@bp.route('/login', methods=('GET', 'POST'))
def login():
    '''
    Verify user login
    '''
    # When login form submitted
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Connect to database
        db = get_db()
        
        # Initialize error message
        error = None
        
        # Query database for user
        user = db.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()
        
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
    

# Register function that runs before view function
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
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    '''
    Lout out user
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
