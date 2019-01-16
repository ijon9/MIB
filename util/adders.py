from flask import Flask
import sqlite3

DB_FILE = "data/database.db"

def add_event(creator, name, month, day, year, clock, location, description, public, alert, priority):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    for i in c.execute("SELECT user FROM calendar WHERE creator = ?, name = ?, month = ?, day = ?, year = ?, clock = ?",(user,name,month,day,year,clock)):
        db.close()
        return "Similar event already exists"
    command = "INSERT INTO calendar (creator, name, month, day, year, clock, location, description, public, alert, priority) VALUES (?,?,?,?,?,?,?,?,?,?,?)"
    args = (creator, name, month, day, year, clock, location, description, public, alert, priority)
    c.execute(command,args)
    db.commit()
    db.close()
