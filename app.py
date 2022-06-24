# Flask development web server application for Word Salad flashcards project
#
# Reference: https://flask.palletsprojects.com/en/2.1.x/quickstart
#
# Import Flask, template 
from flask import Flask, render_template 

# Create instance of class
app = Flask(__name__)

# Set root URL to index page
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')
