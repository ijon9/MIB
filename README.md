# EventBlox:
### MIB - Britni Canale, Mohammed Jamil, Isaac Jon, Mohammed Uddin

## Overview
Our project is a calendar app that allows users to plan tasks or events on specific days on the calendar. 
- User can include many details like the date, time, location, and duration of the event, or tasks to be completed on a certain day. 
- Users will be able to customize reminders that inform them about upcoming dates. 
- Users can also add other users as friends to notify them of your public events, and allow them to RSVP

## Launching the Site
Create a virtual environment:
```
python3 -m venv <venv_name>
```

Activate the virtual environment:
```
. <path to venv>/bin/activate
```

Run this command in our app’s home directory to install all necessary dependencies:
```
(venv)$pip install -r requirements.txt
```

Prepare the database by running:
```
python util/table.py
```

Prepare API Keys:
- Acquire API keys for those found in [API Information](#API-Information)
- Load into the seperate files for each api in the keys folder keys:

```
key_darkSky.json:
{
    "darkSky":"<Insert key here>",
}
key_traffic.json:
{
    "traffic":"<Insert key here>"
}
key_locationIq.json:
{
    "location":"<Insert Key Here>"
}
```
- Then move each file into the root directory



To run the app: 
```
(venv)$python app.py
```

## API Information
- Weather: https://darksky.net/dev
- Traffic: https://developer.mapquest.com/documentation/traffic-api/
- LocationIQ: https://locationiq.com/docs
- Holiday: https://holidayapi.pl/ (key not needed)
- Avatar: http://avatars.adorable.io/ (key not needed)

## Dependencies: 
- Flask: Runs the web application on local host.
- Wheel: Used for Flask.
- SQLite: Creates databases for storing information.
- URLLib3: Receives information from APIs.
- requests: Receives requests from html forms
