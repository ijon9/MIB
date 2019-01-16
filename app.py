import json
import urllib
import random
import os
import ssl
import datetime

from flask import Flask, render_template, session, request, url_for, redirect, flash

from util import auth,getters,adders,account, calendar, friends

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
    return render_template("home.html", avatar=avatar,display= display,todo = todo, m = month, d = day, y = year)


@app.route("/todoitem", methods=["GET"])
def todoitem():
    if "username" in session:
        return redirect(url_for("login"))
    title = request.args["title"]
    month = request.args["month"]
    day = request.args["day"]
    year = request.args["year"]
    time = request.args["time"]
    item = ["Stuff", "More Stuff"]#get_event(session["username"], title , month, day, year, time)
    return render_template("todoitem.html", item = item, title = title, month= month, day = day, year= year, time = time )

@app.route("/login")
def login():
    if "username" in session:
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/calendar")
def cal():
    if "username" not in session:
        return redirect(url_for("login"))
    date = datetime.date.today()
    print(date)
    month = calendar.get_calendar(date.year, date.month, session["username"])
    display=getters.get_display(session["username"])[0]
    avatar=getters.get_avatar(session["username"])[0]
    if avatar==None:
        avatar="https://api.adorable.io/avatars/285/"+session["username"]+".png"
    return render_template("calendar.html",avatar=avatar,display=display, month = month, y =date.year, m = date.month)


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


@app.route("/todo", methods=["GET"])
def todo():
    if "username" not in session:
        return redirect(url_for("login"))
    month = request.args["month"]
    day = request.args["day"]
    year = request.args["year"]
    if int(month)<10:
        month="0"+month
    month=month[0:-1]
    if int(day)<10:
        day="0"+str(day)
    else:
        day=str(day)
    todolist = calendar.get_todo(session["username"], month, day, year)
    print(todolist)
    print(month+ "-" + day + "-" + year)
    return render_template("todo.html", m = month, d = day, year = year, user = session["username"], todo = todolist)

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

@app.route("/requests", methods=["GET", "POST"])
def frq():
    if "username" not in session:
        return redirect(url_for("login"))
    incoming = friends.incoming(session["username"])
    outgoing = friends.outgoing(session["username"])
    display=getters.get_display(session["username"])[0]
    avatar=getters.get_avatar(session["username"])[0]
    if avatar==None:
        avatar="https://api.adorable.io/avatars/285/"+session["username"]+".png"
    for req in incoming:
        if "acc" + req[0] in request.form:
            friends.accept_friend(req[0], session["username"])
            incoming.remove(req)
        if "ign" + req[0] in request.form:
            friends.ignore_friend(req[0], session["username"])
            incoming.remove(req)
    return render_template("requests.html", inc=incoming, out = outgoing, display=display, avatar=avatar)

@app.route("/results", methods=["GET", "POST"])
def res():
    if "username" not in session:
        return redirect(url_for("login"))
    if "sendR" in request.form:
        friends.friend_request(session["username"], request.form["sendR"])
        redirect(url_for("frq"))
    elif "searchRes" in request.form:
        result = friends.get_results(request.form["search"])
        return render_template("results.html", entry=request.form["search"], result=result)
    return render_template("results.html")
if __name__== "__main__":
    app.debug = True
app.run()
