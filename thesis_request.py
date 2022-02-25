import requests
from datetime import date

#r = requests.get(f"http://dt-iotdoorlock.online?filter[appointmentStart]={str(date.today())}")
r = requests.get("http://dt-iotdoorlock.online")
rawData = r.json()

todaysData = []
for i in rawData:
    todaysData.append(i['qrCode'])

def getTodaysData():
    return todaysData













