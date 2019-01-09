import datetime
import requests
def holidays(year,month):
    r=requests.get("https://holidayapi.pl/v1/holidays?country=US&year={0}&month={1}".format(year,month))
    try:
        data=r.json()
    except:
        print("something went wrong")
    return data

#print(holidays(2019,1))

def datify(time):
    t=str(time)
    t=t.replace(" ","T")
    return t
def weather(location,time):
    r=requests.get("https://api.darksky.net/forecast/a0102af2cf0070050894dd64c8980654/{0},{1},{2}".format(location[0],location[1],time))
    try:
        data=r.json()
    except:
        print("something went wrong")
    return data
loc=(40.717716,-74.014039)
#print(weather(loc,"2019-01-09T12:29:17"))