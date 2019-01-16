import json
import urllib
import random
import os
import ssl
import datetime

from flask import Flask, render_template, session, request, url_for, redirect, flash

from util import auth,getters,adders,account, calendar, friends,apihelp

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
        date=request.args["Date"].split("-")
        print("Success Date")
        title = request.args["Title"]
        print("Success Title")
        day = date[1]
        print("Success Day")
        year = date[2]
        print("Success year")
        month = date[0]
        print("Success Month")
        time = request.args["Time"]
        print("Success Time")
        address = request.args["Address"]
        print("Success Address")
        description = request.args["Description"]
        print("Sucess Description")
        priority = request.args["priority"]
        print("Success priority")
        private = request.args["private"]
        print("Success private")
        if "Alerts" in request.args.keys():
            alerts = request.args["Alerts"]
        else:
            alerts = "off"
        print("Success alerts")
        adders.add_event(session["username"], title, day, year, month, time, address, description, private, alerts, priority)
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
    if "username" not in session:
        print("Username not in session<br>")
        return redirect(url_for("login"))
    item = {}
    item["title"] = request.args["title"]
    item["month"] = request.args["month"]
    item["day"] = request.args["day"]
    item["year"] = request.args["year"]
    item["time"]= request.args["time"]
    #priority = request.args["priority"]
    additional = getters.get_event(session["username"], item["title"], item["month"], item["day"], item["year"], item["time"])
    item["description"] = additional[1]
    item["location"] = additional[0]
    item["public"] = additional[2]
    item["alert"] = additional[3]
    item["priority"] = additional[4]
    display=getters.get_display(session["username"])[0]
    avatar=getters.get_avatar(session["username"])[0]
    if avatar==None:
        avatar="https://api.adorable.io/avatars/285/"+session["username"]+".png"
    return render_template("todoitem.html", item = item,display=display,avatar=avatar)

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
    display=getters.get_display(session["username"])[0]
    avatar=getters.get_avatar(session["username"])[0]
    if avatar==None:
        avatar="https://api.adorable.io/avatars/285/"+session["username"]+".png"
    return render_template("todo.html", m = month, d = day, year = year, user = session["username"], todo = todolist,display=display,avatar=avatar)

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

@app.route("/edit", methods=["GET"])
def edit():
    if "username" not in session:
        return redirect(url_for("login"))
    date = request.args["month"]+"/"+request.args["day"]+"/"+request.args["year"]
    description = request.args["description"]
    time = request.args["time"]
    title = request.args["title"]
    address = request.args["location"]
    priority = request.args["priority"]
    display=getters.get_display(session["username"])[0]
    avatar=getters.get_avatar(session["username"])[0]
    if avatar==None:
        avatar="https://api.adorable.io/avatars/285/"+session["username"]+".png"
    return render_template("edit.html", date = date, description = description, time = time, title = title, address = address, priority = priority,display=display,avatar=avatar)



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
            flash("You and " + req[0] + " are now friends!")
        if "ign" + req[0] in request.form:
            friends.ignore_friend(req[0], session["username"])
            incoming.remove(req)
    return render_template("requests.html", inc=incoming, out = outgoing, display=display, avatar=avatar)

@app.route("/results", methods=["GET", "POST"])
def res():
    if "username" not in session:
        return redirect(url_for("login"))
    display=getters.get_display(session["username"])[0]
    avatar=getters.get_avatar(session["username"])[0]
    if avatar==None:
        avatar="https://api.adorable.io/avatars/285/"+session["username"]+".png"
    if "sendR" in request.form:
        friends.friend_request(session["username"], request.form["sendR"])
        flash("You have sent a friend request to " + request.form["sendR"] + "!")
    elif "searchRes" in request.form:
        result = friends.get_results(request.form["search"])
        return render_template("results.html", entry=request.form["search"], result=result, display=display, avatar=avatar)
    return render_template("results.html", display=display, avatar=avatar)

@app.route("/shared",methods=["GET", "POST"])
def shared():
    if "username" not in session:
        return redirect(url_for("login"))
    public=getters.get_public()
    maplist=[]
    for event in public:
        maplist.append(apihelp.getMap(event[6]))
    display=getters.get_display(session["username"])[0]
    avatar=getters.get_avatar(session["username"])[0]
    if avatar==None:
        avatar="https://api.adorable.io/avatars/285/"+session["username"]+".png"

    return render_template("shared.html",public=public,maplist=maplist,display=display,avatar=avatar)
if __name__== "__main__":
    app.debug = True
app.run()
