import json
import urllib
import random
import os
import ssl

from flask import Flask, render_template, session, request, url_for, redirect, flash

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def home():
    #if not session.get("username"):
    #    return redirect(url_for("login"))
    return render_template("home.html", todo = [["1", "Doctor's Appointment", "In 3 Hours", "Eye appointment located in Long Island. Lots of Traffic"], ["2","Doctor's Appointment", "In 3 Hours", "Eye appointment located in Long Island. Lots of Traffic"], ["3","Doctor's Appointment", "In 3 Hours", "Eye appointment located in Long Island. Lots of Traffic"]])

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")


if __name__== "__main__":
    app.debug = True
app.run()
