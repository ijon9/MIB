from flask import Flask
import sqlite3

DB_FILE = "data/database.db"

def get_display(user):
    """
        Returns display name
    """
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT display FROM accts WHERE user = ?"
    args = (user,)
    return c.execute(command,args).fetchone()

def get_avatar(user):
    """
        Returns display name
    """
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT avatar FROM accts WHERE user = ?"
    args = (user,)
    return c.execute(command,args).fetchone()

def get_public():
    """
        Returns a list of lists containing information about each public event
    """
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    return c.execute("SELECT name,month,day,year,clock,location,description FROM calendar WHERE public = 1").fetchall()

listies = get_public()
for thing in listies:
    print(thing[0] + thing[1] + thing[2] + thing[3] + thing[4] + thing[5] + thing[6])
