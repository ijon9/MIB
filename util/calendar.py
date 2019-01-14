from flask import Flask
import sqlite3, calendar

DB_FILE = "data/database.db"

def get_todo(user, day):
    """Returns the to-do list for a specific day"""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT name,time,location,description FROM calendar WHERE creator == ? AND day == ?"
    args = (user,day,)
    return c.execute(command,args).fetchall()


def get_calendar(year, month, user):
    cal = calendar.Calendar(6).monthdatescalendar(year, month)
    calendar = []
    w = 0
    d = 0
    for week in cal:
        calendar[w] = {}
        w = w+1
        d = 0
        for day in week:
            calendar[w][d] = [day[2], get_todo(user, year, month, day[2])
            d = d + 1
