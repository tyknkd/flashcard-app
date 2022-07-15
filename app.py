# Flask development web server application for Word Salad flashcards project
#
# Reference: https://flask.palletsprojects.com/en/2.1.x/quickstart
#
# Import Flask, template, reverse URL class
import dbScripts.createDB as createDB
import dbScripts.initialPopulate as initialPopulate

from flask import Flask, render_template, url_for

# Create instance of class
app = Flask(__name__)

# Set root URL to index page
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

#Create Database as flashcards.db
dbName = "flashcards.db"
sql = createDB.getSQL(".\dbScripts\MySQLCreate.sql")
createDB.createDB(dbName, sql)
print('Database', dbName, "created successfully")

#Populate tables with decks in Decks folder
decks = ["GRE_vocab.csv", "LSAT_vocab.csv","SAT_vocab.csv"]
initialPopulate.addWordSaladSuperUser("flashcards.db")
for deck in decks:
    initialPopulate.populateCards("flashcards.db", deck)
    print(deck, "used to successfully populate tables")
