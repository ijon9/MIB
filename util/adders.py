from flask import Flask
import sqlite3

DB_FILE = "data/database.db"

def add_event(creator, name, time, frequency, location, description, public, alert, priority){
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "INSERT INTO calendar (creator, name, time, frequency, location, description, public, alert, priority) VALUES (?,?,?,?,?,?,?,?,?)"
    args = (creator, name, time, frequency, location, description, public, alert, priority);
    c.execute(command,args)
    db.commit()
    db.close()
}