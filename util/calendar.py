from flask import Flask
import sqlite3, calendar

from util import table

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
        d = 0
        for day in week:
            stryear=str(year)
            strmonth=""
            strday=""
            if month<10:
                strmonth="0"+str(month)
            else:
                strmonth=str(month)
            if day.day<10:
                strday="0"+str(day.day)
            else:
                strday=str(day.day)
            print(strday)
            monthcalendar[w][d] = [day.day, get_todo(user, strmonth, strday, stryear)]
            print(get_todo(user, strmonth, strday, stryear))
            d = d+1
        w = w+1
    print(monthcalendar)
    return monthcalendar

def remove_event(user, name, month, day, year, clock):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "DELETE FROM calendar WHERE creator == ? AND name == ? AND year == ? AND month == ? AND day == ? AND clock == ?"
    args = (user,name,year,month,day,clock,)
    c.execute(command,args)
    db.commit()
    db.close()
    
