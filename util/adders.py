from flask import Flask
import sqlite3

DB_FILE = "data/database.db"

def add_event(user, name, month, day, year, clock, location, description, public, alert, priority):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "INSERT INTO calendar (user, name, month, day, year, clock, location, description, public, alert, priority, complete) VALUES (?,?,?,?,?,?,?,?,?,?,?,0)"
    args = (user, name, month, day, year, clock, location, description, public, alert, priority)
    c.execute(command,args)
    db.commit()
    db.close()
