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

"""
def get_public():
    """"""
        Returns a list of lists containing information about each public event
    """"""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    return c.execute("SELECT user,name,month,day,year,clock,location,description FROM calendar WHERE public = public").fetchall()
"""

def helpyboi(listyboi):
    """
        is key for sorted function, returns concatenated string to be ordered
    """
    return listyboi[4] + listyboi[2] + listyboi[3] + listyboi[5] #year+month+day+time

def get_public():
    """
        Returns a list of lists containing information about each public event, sorted by date and time
    """
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    listybois = c.execute("SELECT user,name,month,day,year,clock,location,description FROM calendar WHERE public = public").fetchall()
    return sorted(listybois, key=helpyboi)


def get_event(user, name, month, day, year, clock):
    """
        Returns a list of information about a specific event
    """
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT location,description,public,alert,priority FROM calendar WHERE user = ? AND name = ? AND month = ? AND day = ? AND year = ? AND clock = ?"
    args = (user, name, month, day, year, clock)
    return c.execute(command, args).fetchone()
