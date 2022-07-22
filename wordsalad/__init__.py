# Flask development web server application factory for Word Salad flashcards project
# Sets up configuration and returns Flask app
# Note: Filename `__init__.py` tells Python that `wordsalad` directory is a package 
# Reference: https://flask.palletsprojects.com/en/2.1.x/tutorial/factory/
#
# Import Flask, template, reverse URL class
from flask import Flask, render_template, url_for
#
# Library to handle operating system paths
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

    # Hello page for unit testing app factory
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # Import/register database initialization script
    from . import db
    db.init_app(app)
    
    # Import/register authentication Blueprint
    from . import auth
    app.register_blueprint(auth.bp)
    # app.add_url_rule('/auth/', endpoint='auth.index')
    
    # Import/register home Blueprint
    from . import home
    app.register_blueprint(home.bp)
    app.add_url_rule('/', endpoint='index')

    # Import/register decks Blueprint
    from . import decks
    app.register_blueprint(decks.bp)
    app.add_url_rule('/decks/', endpoint='decks.index')

    return app

