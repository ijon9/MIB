import datetime
import requests
import json

def holidays(year,month):
    '''
        Gets a dictionary of holidays for a certain month and year
    '''
    url="https://holidayapi.pl/v1/holidays"
    data={
        "country":"US",
        "year":year,
        "month":month,
    }
    r=requests.get(url,params=data)
    try:
        response=r.json()
    except:
        print("something went wrong")
    return response

print(holidays(2019,1))

def datify(time):
    '''
        This function accepts a datetime object and converts that into a string that will work with the Dark Sky API
    '''
    t=str(time)
    t=t.replace(" ","T")
    t=t.split(".")[0]
    return t
def weather(location,time):
    '''
        This function gets the weather and temperature for a certain place at a certain time via the Dark Sky API
        The locations should be a tuple containting the longitude and latitude for example (latitude, longitude)
        The time should be a datetime object
    '''
    with open("keys.json") as f:
        DarkSkyKey = json.load(f)["darkSky"]
    time=datify(time)
    r=requests.get("https://api.darksky.net/forecast/{0}/{1},{2},{3}".format(DarkSkyKey,location[0],location[1],time))
    try:
        data=r.json()
    except:
        print("something went wrong")
    weather=[]
    weather.append(data["currently"]["summary"])
    weather.append(int(data["currently"]["temperature"]))
    return weather
def getGeocode(address):
    '''
        Returns the longitude and latitude for a given address
    '''
    url = "https://us1.locationiq.com/v1/search.php"
    with open("keys.json") as f:
        locationKey = json.load(f)["location"]
    data = {
        'key': locationKey,
        'q': address,
        'format': 'json'
    }
    r = requests.get(url, params=data)
    response=r.json()
    loc=[]
    loc.append(float(response[0]["lat"]))
    loc.append(float(response[0]["lon"]))
    return loc
def traffic(location):
    '''
        Returns traffic incidents near a given location
    '''
    url="https://www.mapquestapi.com/traffic/v2/incidents"
    with open("keys.json") as f:
        trafficKey = json.load(f)["traffic"]
    data={
        "outFormat":"json",
        "key":trafficKey,
        "boundingBox":"{0},{1},{2},{3}".format(location[0],location[1],location[0]+0.03,location[1]+0.03),
        "filters":"incidents,construction,congestion,event"
    }
    r=requests.get(url,params=data)
    response=r.json()
    incidentlist=[]
    for incident in response["incidents"]:
        incidentlist.append(incident["shortDesc"])
    return incidentlist

loc=getGeocode("Stuyvesant High School")
print(weather(loc,datetime.datetime.now()))
print(traffic(loc))
