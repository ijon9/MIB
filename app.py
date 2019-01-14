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
        adders.add_event(session["username"], request.args["Title"], request.args["Date"][0:2], request.args["Date"][3:5], request.args["Date"][6:], request.args["Time"], request.args["Address"], request.args["Description"], request.args["private"], request.args["Alerts"], request.args["priority"])
        print("Added")
    display=getters.get_display(session["username"])[0]
    avatar=getters.get_avatar(session["username"])[0]
    if avatar==None:
        avatar="https://api.adorable.io/avatars/285/"+session["username"]+".png"
    date = datetime.date.today()
    print(date.month)
    todo = calendar.get_todo(session["username"], date.month, date.day, date.year)
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
    month = calendar.get_calendar(date[0], date[1], session["username"])
    display=getters.get_display(session["username"])[0]
    avatar=getters.get_avatar(session["username"])[0]
    if avatar==None:
        avatar="https://api.adorable.io/avatars/285/"+session["username"]+".png"
    return render_template("calendar.html",avatar=avatar,display=display, month = month)


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
    return render_template("add.html")


if __name__== "__main__":
    app.debug = True
app.run()
