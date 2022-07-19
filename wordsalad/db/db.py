#!/usr/bin/python3

# Database connection script
#
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/database/

import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


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
