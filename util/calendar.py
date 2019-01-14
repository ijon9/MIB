from flask import Flask
import sqlite3

DB_FILE = "data/database.db"

def get_todo(user, day):
    """Returns the to-do list for a specific day"""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT name,day,clock,location,description FROM calendar WHERE creator == ? AND day == ?"
    args = (user,day,)
    return c.execute(command,args).fetchall()
