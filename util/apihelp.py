import datetime
import requests
DarkSkyKey="a0102af2cf0070050894dd64c8980654"
def holidays(year,month):
    '''
        Gets a dictionary of holidays for a certain month and year
    '''
    r=requests.get("https://holidayapi.pl/v1/holidays?country=US&year={0}&month={1}".format(year,month))
    try:
        data=r.json()
    except:
        print("something went wrong")
    return data

#print(holidays(2019,1))

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
    time=datify(time)
    print(time)
    r=requests.get("https://api.darksky.net/forecast/{0}/{1},{2},{3}".format(DarkSkyKey,location[0],location[1],time))
    try:
        data=r.json()
    except:
        print("something went wrong")
    weather=[]
    weather.append(data["currently"]["summary"])
    weather.append(int(data["currently"]["temperature"]))
    return weather
loc=(40.717716,-74.014039)
print(weather(loc,datetime.datetime.now()))
