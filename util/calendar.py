from flask import Flask
import sqlite3, calendar

from util import table

DB_FILE = "data/database.db"


def get_todo(user, month, day, year):
    """Returns the to-do list for a specific day"""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT name,month,day,year,clock,location,description FROM calendar WHERE user == ? AND year == ? AND month == ? AND day == ?"
    args = (user,year,month,day,)
    return c.execute(command,args).fetchall()


def get_calendar( user):
    totalcal={}
    for year in range(2018,2024):
        totalcal[year] = {}
        for month in range(1, 13):
            totalcal[year][month] = {}
            cal = calendar.Calendar(6).monthdatescalendar(year, month)
            wk = 0
            d = 0
            for week in cal:
                totalcal[year][month][wk] = {}
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
                    totalcal[year][month][wk][d] = [day.day, get_todo(user, strmonth, strday, stryear)]
                    d = d+1
                wk = wk+1
    return totalcal

def remove_event(user, name, month, day, year, clock):
    print("TRYING TO DELETE")
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    print(user)
    command = "DELETE FROM calendar WHERE user == ? AND name == ? AND year == ? AND month == ? AND day == ? AND clock == ?"
    params = (user,name,year,month,day,clock)
    print(params)
    c.execute(command,params)
    db.commit()
    db.close()
    print("DELETE COMPLETE")

def edit_event(user, name, month, day, year, clock, info):
    print("TRYING TO Edit")
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "UPDATE calendar SET name = ?,month = ?,day = ?,year = ?,clock = ?,location = ?,description = ?,public = ?,alert = ?,priority = ? WHERE user == ? AND name == ? AND year == ? AND month == ? AND day == ? AND clock == ?"
    args = (info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8],info[9],user,name,month,day,year,clock)
    print(args)
    c.execute(command,args)
    db.commit()
    db.close()
    return "Edited"
