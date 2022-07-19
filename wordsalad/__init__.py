# Flask development web server application factory for Word Salad flashcards project
# Sets up configuration and returns Flask app
# Note: Filename `__init__.py` tells Python that `wordsalad` directory is a package 
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/factory/
#
# Import Flask, template, reverse URL class
from flask import Flask, render_template, url_for

import os

def create_app(test_config=None):
    # Create and configure app instance
    # __name__: name of current Python module
    # instance_relative_config=True: config files in instance folder above /wordsalad/
    app = Flask(__name__, instance_relative_config=True)

    # Set default configuration
    # DATABASE: path to SQLite database file (instance folder)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'wordsalad.sqlite'),
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        # config.py overrides default configuration (e.g., more secure SECRET_KEY)
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # Check that the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    # Set root URL to index page
    @app.route('/')
    @app.route('/index.html')
    def index():
        return render_template('index.html')

    # Set route to about page
    @app.route('/about/')
    def about():
        return render_template('about.html')

    # Set route to login page
    @app.route('/login/')
    def login():
        return render_template('login.html')

    # Set route to decks page
    @app.route('/decks/')
    def decks():
        return render_template('decks.html')

    # Set route to /decks/<deck_name> page
    @app.route('/decks/<deck_name>')
    def show_deck(deck_name):
        return render_template('<deck_name>.html')

    # Set route to /edit/<deck_name> page
    @app.route('/edit/<deck_name>')
    def edit_deck(deck_name):
        return render_template('edit.html')

    # Register database initialization script
    from .dbScripts import db
    db.init_app(app)
    
    # Register authentication Blueprint
    from . import auth
    app.register_blueprint(auth.bp)

    return app


#Create Database as flashcards.db
#dbName = "wordsalad.db"
#sql = makeDB.getSQL("/db/schema.sql")
#makeDB.createDB(dbName, sql)
#print('Database', dbName, "created successfully")

#Populate tables with decks in /db/data folder
#decks = ["GRE_vocab.csv", "LSAT_vocab.csv","SAT_vocab.csv"]
#makeDB.addWordSaladSuperUser(dbName)
#for deck in decks:
#    makeDB.populateCards(dbName, deck)
#    print(deck, "used to successfully populate tables")
