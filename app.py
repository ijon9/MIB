import json
import urllib
import random
import os
import ssl
import datetime

from flask import Flask, render_template, session, request, url_for, redirect, flash

from util import auth,getters,adders,account, calendar

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/",methods=["POST","GET"])
def home():
    if "login" in request.form:
        message=auth.login(request.form["user"],request.form["pass"])
        flash(message)
        if message!="Login successful":
            return redirect(url_for("login"))
        else:
            session["username"]=request.form["user"]
    if "register" in request.form:
        message=auth.register(request.form["user"],request.form["pass"],request.form["confirmpass"],request.form["display"])
        flash(message)
        return redirect(url_for("login"))
    if "username" not in session:
        return redirect(url_for("login"))
    if "additems" in request.args:
        print(request.args)
        try:
            date=request.args["Date"].split("-")
            adders.add_event(session["username"], request.args["Title"], date[1], date[2], date[0], request.args["Time"], request.args["Address"], request.args["Description"], request.args["private"], request.args["Alerts"], request.args["priority"])
        except:
            flash("Something went wrong")
        print("Added")
    display=getters.get_display(session["username"])[0]
    avatar=getters.get_avatar(session["username"])[0]
    if avatar==None:
        avatar="https://api.adorable.io/avatars/285/"+session["username"]+".png"
    date = datetime.date.today()
    year=str(date.year)
    month=""
    day=""
    if date.month<10:
        month="0"+str(date.month)
    else:
        month=str(month)
    if date.day<10:
        day="0"+str(date.day)
    else:
        day=str(date.day)
    todo = calendar.get_todo(session["username"], month, day, year)
    print(todo)
    return render_template("home.html", avatar=avatar,display= display,todo = todo)

@app.route("/login")
def login():
    if "username" in session:
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/calendar")
def cal():
    if "username" not in session:
        return redirect(url_for("login"))
    date = datetime.date.today().isocalendar()
    print(date)
    month = calendar.get_calendar(date[0], date[2], session["username"])
    display=getters.get_display(session["username"])[0]
    avatar=getters.get_avatar(session["username"])[0]
    if avatar==None:
        avatar="https://api.adorable.io/avatars/285/"+session["username"]+".png"
    return render_template("calendar.html",avatar=avatar,display=display, month = month, y =date[0], m = date[2])


@app.route("/account",methods=["POST","GET"])
def acc():
    if "username" not in session:
        return redirect(url_for("login"))
    if "dischange" in request.form:
        message=account.change_display(session["username"],request.form["display"])
        flash(message)
    if "picchange" in request.form:
        message=account.change_avatar(session["username"],request.form["pic"])
        flash(message)
    if "passchange" in request.form:
        message=account.change_password(session["username"],request.form["oldpass"],request.form["newpass"],request.form["cnewpass"])
        print(message)
        flash(message)
    display=getters.get_display(session["username"])[0]
    avatar=getters.get_avatar(session["username"])[0]
    if avatar==None:
        avatar="https://api.adorable.io/avatars/285/"+session["username"]+".png"
    return render_template("account.html",avatar=avatar,display=display)


@app.route("todo", methods=["GET"])
def todo():
    if "username" not in session:
        return redirect(url_for("login"))
    month = request.args["month"]
    day = request.args["day"]
    year = request.args["year"]
    todolist = calendar.get_todo(session["username"], month, day, year)
    print(todolist)
    return render_template("todo.html", m = month, d = day, year = year, user = session["username"])

@app.route("/logout")
def logout():
    try:
        session.pop('username')
        flash("You have successfully logged out")
        return redirect(url_for("login"))
    except:
        flash("You have successfully logged out")
        return redirect(url_for("login"))

@app.route("/add")
def add():
    if "username" not in session:
        return redirect(url_for("login"))
    display=getters.get_display(session["username"])[0]
    avatar=getters.get_avatar(session["username"])[0]
    if avatar==None:
        avatar="https://api.adorable.io/avatars/285/"+session["username"]+".png"
    return render_template("add.html",display=display,avatar=avatar)


if __name__== "__main__":
    app.debug = True
app.run()
