#!/usr/bin/python3

# Database connection, initialization, registration scripts
#
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/database/

import sqlite3

# Click command line interface
# https://click.palletsprojects.com/en/8.1.x/api/
import click

from flask import current_app, g
from flask.cli import with_appcontext


# Create database connection
def get_db():
    # If database connection is not already stored in namespace object `g`
    if 'db' not in g:
        # Create connection to `DATABASE` specified by app pointed to by `current_app`
        # and store in `g`
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # Return rows as dictionary objects
        g.db.row_factory = sqlite3.Row

    return g.db


# If connection exists, close it
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


# Initialize database using `schema.sql`
def init_db():
    db = get_db()

    # Open `schema.sql` relative to app pointed to by `current_app`
    with current_app.open_resource('schema.sql') as f:
        # Execute SQL commands in `schema.sql` 
        db.executescript(f.read().decode('utf8'))


# Create command line command to call `init-db`
@click.command('init-db')
@with_appcontext
def init_db_command():
    '''
    Clear the existing data and create new tables
    '''
    init_db()
    click.echo('Initialized the database.')
    
    
# Register `close_db` and `init_db_command` functions with 
# Flask app instance
def init_app(app):
    # Instruct Flask to call `close_db` after returning response
    app.teardown_appcontext(close_db)
    # Add `init_db_command` to be called with `flask` command
    app.cli.add_command(init_db_command)
