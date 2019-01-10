from flask import Flask
import sqlite3

DB_FILE = "data/database.db"

def change_avatar(user, image):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("UPDATE accts SET avatar = ? WHERE user = ?",(image,user,)
    db.commit()
    db.close()
    return "Avatar updated"

def change_password(user, old, new, conf):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    if pass != conf:
        return "Passwords do not much"
    for i in c.execute("SELECT password FROM accts WHERE user = ?",(user,)):
        if i[0] != old:
            db.close()
            return "Incorrect password"
    c.execute("UPDATE accts SET password = ? WHERE user = ?",(new,user,)
    db.commit()
    db.close()
    return "Password updated"

def change_display(user, display):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("UPDATE accts SET display = ? WHERE user = ?",(display,user,)
    db.commit()
    db.close()
    return "Name updated"
