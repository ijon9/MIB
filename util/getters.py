userfrom flask import Flask
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
    return c.execute("SELECT user,name,month,day,year,clock,location,description FROM calendar WHERE public = public").fetchall()

def get_event(user, name, month, day, year, clock):
    """
        Returns a list of information about a specific event
    """
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT location,description,public,alert,priority FROM calendar WHERE creator = ? AND name = ? AND month = ? AND day = ? AND year = ? AND clock = ?"
    args = (user, name, month, day, year, clock)
    return c.execute(command, args).fetchone()
