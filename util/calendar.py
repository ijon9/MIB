from flask import Flask
import sqlite3, calendar

DB_FILE = "data/database.db"


def get_todo(user, month, day, year):
    """Returns the to-do list for a specific day"""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT name,month,day,year,clock,location,description FROM calendar WHERE creator == ? AND year == ? AND month == ? AND day == ?"
    args = (user,year,month,day,)
    return c.execute(command,args).fetchall()


def get_calendar(year, month, user):
    cal = calendar.Calendar(6).monthdatescalendar(year, month)
    monthcalendar = {}
    w = 0
    d = 0
    for week in cal:
        monthcalendar[w] = {}
        w = w+1
        d = 0
        for day in week:
            monthcalendar[w][d] = [day.day, get_todo(user, year, month, day.day)]
            d = d+1
    return monthcalendar

print(get_calendar(2019, 1, "cool"))
