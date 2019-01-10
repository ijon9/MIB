from flask import Flask
import sqlite3

DB_FILE = "data/database.db"

def register(user, pass, conf, display):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    if pass != conf:
        return "Passwords do not match"
    for i in c.execute("SELECT user FROM accts WHERE user = ? ",(user,)):
        db.close()
        return "Username already exists"
    c.execute("INSERT INTO accts (user, password, display) VALUES(?,?,?)", (user,pwd,display,))
    db.commit()
    db.close()
    return "Account creation successful"

def login(user, pass):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    for i in c.execute("SELECT password FROM accts WHERE user = ?",(user,)):
        if i[0] == pass:
            db.close()
            return "Login successful"
        else:
            db.close()
            return "Incorrect password"
    db.close()
    return "Username does not exist"
