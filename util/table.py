import sqlite3

DB_FILE = "data/database.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

"""Create the database if not already created"""

command = "CREATE TABLE IF NOT EXISTS accts(user TEXT, password TEXT, display TEXT, avatar TEXT)"
c.execute(command)

command = "CREATE TABLE IF NOT EXISTS friends(username TEXT, friend TEXT, accepted INTEGER)"
c.execute(command)

command = "CREATE TABLE IF NOT EXISTS calendar(creator TEXT, name TEXT, month TEXT, day TEXT, year TEXT, clock TEXT, location TEXT, description TEXT, public INTEGER, alert TEXT, priority INTEGER)"
c.execute(command)

db.commit()
db.close()
