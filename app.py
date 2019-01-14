import json
import urllib
import random
import os
import ssl
import datetime

from flask import Flask, render_template, session, request, url_for, redirect, flash

from util import auth, calendar

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
    return render_template("home.html", todo = [["1", "Doctor's Appointment", "In 3 Hours", "Eye appointment located in Long Island. Lots of Traffic"], ["2","Doctor's Appointment", "In 3 Hours", "Eye appointment located in Long Island. Lots of Traffic"], ["3","Doctor's Appointment", "In 3 Hours", "Eye appointment located in Long Island. Lots of Traffic"]])

@app.route("/login")
def login():
    if "username" in session:
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/calendar")
def cal():
    date = datetime.date.today().isocalendar()
    month = calendar.get_calendar(date[0], date[1])
    return render_template("calendar.html",month = month)


@app.route("/logout")
def logout():
    try:
        session.pop('username')
        flash("You have successfully logged out")
        return redirect(url_for("login"))
    except:
        flash("You have successfully logged out")
        return redirect(url_for("login"))

if __name__== "__main__":
    app.debug = True
app.run()
