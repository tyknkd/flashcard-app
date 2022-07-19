import sqlite3

#Returns card information in a list from a card Id
#Format = [category, front, back, notes]
def getCard(dbName, cardId):
    db = "./database/" + dbName
    conn = sqlite3.connect(db)
    c = conn.cursor()

    cardSQL = "SELECT category, front, back, notes FROM flashcards WHERE card_id = ?"
    c.execute(cardSQL, cardId)
    ret = c.fetchone()
    c.close()
    return ret

#Returns name, username and email from a user Id
def getUser(dbName, userId):
    db = "./database/" + dbName
    conn = sqlite3.connect(db)
    c = conn.cursor()

    userSQL = "SELECT name, username, email FROM users WHERE user_id = ?"
    c.execute(userSQL, userId)
    ret = c.fetchone()
    c.close()
    return ret

#Returns aname, category, owner_id, public from a single deck
def getDeck(dbName, deckId):
    db = "./database/" + dbName
    conn = sqlite3.connect(db)
    c = conn.cursor()

    deckSQL = "SELECT name, category, owner_id, public from decks WHERE deck_id = ?"
    c.execute(deckSQL, deckId)
    ret = c.fetchone()
    c.close()
    return ret
    

#Returns list of cards created by a specified user
def getUserCards(dbName, userId):
    db = "./database/" + dbName
    conn = sqlite3.connect(db)
    c = conn.cursor()

    ccbuSQL = "SELECT DISTINCT card_id from cards_created_by_users WHERE user_id = ?"
    c.execute(ccbuSQL, userId)
    ret = c.fetchall()
    c.close()
    return ret

#Returns list of cards in a specifed deck
def getCardsInDeck(dbName, deckId):
    db = "./database/" + dbName
    conn = sqlite3.connect(db)
    c = conn.cursor()

    cidSQL = "SELECT DISTINCT card_id from cards_in_deck WHERE deck_id = ?"
    c.execute(cidSQL, deckId)
    ret = c.fetchall()
    c.close()
    return ret

#Returns a list of deck Ids associated with a User Id
def getUserDecks(dbName, userId):
    db = "./database/" + dbName
    conn = sqlite3.connect(db)
    c = conn.cursor()

    cidSQL = "SELECT DISTINCT deck_id from decks WHERE user_id = ?"
    c.execute(cidSQL, userId)
    ret = c.fetchall()
    c.close()
    return ret