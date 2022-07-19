#!/usr/bin/python3

# Python script to create Blueprint to handle authentication requests to app 
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/views/

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from wordsalad.dbScripts.db import get_db

# Create Blueprint
bp = Blueprint('auth', __name__, url_prefix='/auth')
