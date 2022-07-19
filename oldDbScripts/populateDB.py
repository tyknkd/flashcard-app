#!/usr/bin/python3

# Script to create and populate database for Word Salad flashcard app

import sqlite3
import csv

# Use db.py to initialize database
#def getSQL(filename):
#    file = open(filename, 'r')
#    sql = file.read()
#    file.close()
#    return sql
#
#def createDB(dbName, sql):
#    db = "./database/"+dbName
#    conn = sqlite3.connect(db)
#    c = conn.cursor()
#
#    c.executescript(sql)
#    conn.commit()
#

## TO DO: Change database path relative to Flask instance
## See: https://flask.palletsprojects.com/en/2.1.x/tutorial/database/

#Helper function to read the deck csv files
def readCSVFile(filename):
    csvContents = []
    with open (filename, 'r', newline='') as csvFile:
        file = csv.reader(csvFile, delimiter=',')
        for line in file:
            csvContents.append(line)
        
    return csvContents

#Adds the Super User who will have created our initial decks
def addWordSaladSuperUser(dbName):
    #Initiate DB Connection
    db = "./database/"+ dbName
    conn = sqlite3.connect(db)
    c = conn.cursor()

    sql = "INSERT INTO users values (1, 'Word Salad', 'Word_Salad','Word@Salad.Salad')"
    c.execute(sql)

#Populates flashcards, decks, cards_in_deck and cards_created_by_users table with
#cards from a csvfile
def populateCards (dbName, csvFile):
    #Filepath + Name of Card Deck
    csvPath = "data\\" + csvFile
    deckName = csvFile.removesuffix('.csv')

    #Get contents of Deck List
    csvContents = readCSVFile(csvPath)
    csvContents.pop(0)

    #Initiate DB Connection
    db = "./database/"+ dbName
    conn = sqlite3.connect(db)
    c = conn.cursor()

    #Insert cards into flashcards table
    cardSql = "INSERT INTO flashcards (category, front, back, notes) VALUES (?,?,?,?)"
    for line in csvContents:
        data = [line[1],line[0],line[2],deckName]
        c.execute(cardSql, data)
    conn.commit()

    #Create deck for cards
    deckSql = "INSERT INTO decks (name, category, owner_id) VALUES (?,?,?)"
    deckData = [deckName, deckName, 1]

    c.execute(deckSql, deckData)
    conn.commit()

    #Get list of Card Ids
    cardQuery = "SELECT card_id FROM flashcards WHERE notes=?"
    c.execute(cardQuery,(deckName,))
    cardIds = c.fetchall()
    deckQuery = "SELECT deck_id FROM decks WHERE name=? LIMIT 1"
    c.execute(deckQuery, (deckName,))
    deckId = c.fetchall()

    #Put list of cards into cards_in_deck and cards_created_by_users tables
    cidSql = "INSERT INTO cards_in_deck (card_id, deck_id) VALUES (?,?)"
    ccbuSql = "INSERT INTO cards_created_by_users (user_id, card_id) VALUES (?,?)"
    for cardId in cardIds:
        cidEntry = [cardId[0], deckId[0][0]]
        ccbuEntry = [1,cardId[0]]
        c.execute(cidSql, cidEntry)
        c.execute(ccbuSql,ccbuEntry)
    conn.commit()
