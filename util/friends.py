from flask import Flask
import sqlite3

DB_FILE = "data/database.db"

friend_request(user1, user2):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO friends (username, friend, accepted) VALUES (?,?,0)",(user1,user2,))
    db.commit()
    db.close()

accept_friend(user1, user2):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("UPDATE friends SET accepted = 1 WHERE user1 == ? AND user2 == ? OR user1 == ? AND user2 == ?",(user1,user2,user2,user1,))
    db.commit()
    db.close()
