import os
from unicodedata import name
# from flask import Flask
from wordsalad import create_app 
from wordsalad import db

app = create_app()

if __name__== "__main_":
    db.init_app(app) 
    app.run()