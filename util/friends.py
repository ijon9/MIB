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
    c.execute("UPDATE friends SET accepted = 1 WHERE username == ? AND friend == ?",(user1,user2,))
    db.commit()
    db.close()

def ignore_friend(user1, user2):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("UPDATE friends SET accepted = 3 WHERE username == ? AND friend == ?",(user1,user2,))
    db.commit()
    db.close()

def friend_list():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    return c.execute("SELECT display FROM accts").fetchall()

def outgoing(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    return c.execute("SELECT friend FROM friends WHERE username == ? AND accepted == ?",(user, 0)).fetchall()

def incoming(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    return c.execute("SELECT username FROM friends WHERE friend == ? AND accepted == ?",(user, 0)).fetchall()
