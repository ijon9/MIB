import json
import urllib
import random
import os
import ssl

from flask import Flask, render_template, session, request, url_for, redirect, flash

from util import auth,getters,adders,account

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
    display=getters.get_display(session["username"])[0]
    avatar=getters.get_avatar(session["username"])[0]
    if avatar==None:
        avatar="https://api.adorable.io/avatars/285/"+session["username"]+".png"
    return render_template("home.html", avatar=avatar,display= display,todo = [["1", "Doctor's Appointment", "In 3 Hours", "Eye appointment located in Long Island. Lots of Traffic"], ["2","Doctor's Appointment", "In 3 Hours", "Eye appointment located in Long Island. Lots of Traffic"], ["3","Doctor's Appointment", "In 3 Hours", "Eye appointment located in Long Island. Lots of Traffic"]])

@app.route("/login")
def login():
    if "username" in session:
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/calendar")
def calendar():
    display=getters.get_display(session["username"])[0]
    avatar=getters.get_avatar(session["username"])[0]
    if avatar==None:
        avatar="https://api.adorable.io/avatars/285/"+session["username"]+".png"
    return render_template("calendar.html",avatar=avatar,display=display)
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

if __name__== "__main__":
    app.debug = True
app.run()
