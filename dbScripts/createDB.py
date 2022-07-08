import sqlite3

def getSQL(filename):
    file = open(filename, 'r')
    sql = file.read()
    file.close()
    return sql

def createDB(dbName, sql):
    db = "./database/"+dbName
    conn = sqlite3.connect(db)
    c = conn.cursor()

    c.executescript(sql)
    conn.commit()

sql = getSQL(".\dbScripts\MySQLCreate.sql")
createDB("flashcards.db", sql)