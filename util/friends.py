from flask import Flask
import sqlite3

DB_FILE = "data/database.db"

def request_present(user1, user2):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    l = []
    l.append(c.execute("SELECT username,friend FROM friends WHERE (username == ? AND friend == ?) or (username == ? AND friend == ?)",(user1, user2, user2, user1)).fetchone())
    if l[0] == None:
        return False
    else:
        return True

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
    c.execute("UPDATE friends SET accepted = 2 WHERE username == ? AND friend == ?",(user1,user2,))
    db.commit()
    db.close()

def request_denied(user1, user2):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("UPDATE friends SET accepted = 3 WHERE username == ? AND friend == ?",(user1,user2,))
    db.commit()
    db.close()

def outgoing(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    return c.execute("SELECT friend,accepted FROM friends WHERE (username == ? AND accepted == ?) OR (username == ? AND accepted == ?)",(user, 0,user,2)).fetchall()

def incoming(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    return c.execute("SELECT username FROM friends WHERE friend == ? AND accepted == ?",(user, 0)).fetchall()

def get_results(user,entry):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    userList = c.execute("SELECT user FROM accts").fetchall()
    possUsers = []
    for u in userList:
        if entry in u[0]:
            possUsers.append(u[0])
    res = []
    for possU in possUsers:
        if user == possU:
            pass
        else:
            n = []
            n.append(c.execute("SELECT user,display,avatar FROM accts WHERE user == ?",(possU,)).fetchone())
            if request_present(user, possU):
                n.append("F")
            else:
                n.append("NF")
            res.append(n)
    return res
