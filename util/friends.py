from flask import Flask
import sqlite3

DB_FILE = "data/database.db"

def friend_request(user1, user2):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO friends (username, friend, accepted) VALUES (?,?,0)",(user1,user2,))
    db.commit()
    db.close()

def accept_friend(user1, user2):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("UPDATE friends SET accepted = 1 WHERE user1 == ? AND user2 == ? OR user1 == ? AND user2 == ?",(user1,user2,user2,user1,))
    db.commit()
    db.close()

def friend_list():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    return c.execute("SELECT display FROM accts").fetchall()
