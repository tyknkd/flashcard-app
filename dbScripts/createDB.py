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

dbName = "flashcards.db"
sql = getSQL(".\dbScripts\MySQLCreate.sql")
createDB(dbName, sql)
print('Database', dbName, "created successfully")