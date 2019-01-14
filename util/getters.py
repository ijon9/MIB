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
