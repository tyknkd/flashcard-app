import sqlite3

#Adds a card to flashcards and an entry to cards_created_by_users
def addCard(dbName, userId, word, definition, category, notes):
    cardTableSql = "INSERT INTO flashcards (category, front, back, notes) VALUES (?,?,?,?)"
    userCardSql = "INSERT INTO cards_created_by_users (user_id, card_id) VALUES (?,?)"

    db = "./database/" + dbName
    conn = sqlite3.connect(db)
    c = conn.cursor()

    #Inserts new card into the flashcards table
    c.execute(cardTableSql, [category, word, definition, notes])
    rowId = c.lastrowid()

    #Gets the cardId from the previous insert and uses it to write a row to the 
    #Cards_created_by_users table
    c.execute(userCardSql, [userId, rowId])
    conn.commit()
    c.close()

#Adds a deck to decks
def addDeck(dbName, name, category, userId):
    deckTableSql = "INSERT INTO decks (name, category, owner_id) VALUES (?,?,?)"

    db = "./database/" + dbName
    conn = sqlite3.connect(db)
    c = conn.cursor()

    c.execute(deckTableSql, [name, category, userId])
    conn.commit()
    c.close()


#Adds a user to users
#TODO for another function? - ensure username or email is not already in use
def addUser(dbName, name, username, email):
    userTableSql = "INSERT INTO users (name, username, email) values (?,?,?)"

    db = "./database/"+ dbName
    conn = sqlite3.connect(db)
    c = conn.cursor()

    c.execute(userTableSql, [name, username, email])
    conn.commit()
    c.close()


#Adds cards to specific decks
#TODO for another function - check if a card already exists in a deck
def addCardToDeck(dbName, deckId, cardId):
    cidTableSql = "INSERT INTO cards_in_deck (card_id, deck_id) VALUES (?,?)"

    db = "./database/"+ dbName
    conn = sqlite3.connect(db)
    c = conn.cursor()

    c.execute(cidTableSql, [cardId, deckId])
    conn.commit()
    c.close()
