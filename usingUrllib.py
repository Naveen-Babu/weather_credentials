
import urllib.request, urllib.parse, urllib.error
import json, requests

url = 'http://api.openweathermap.org/data/2.5/weather?q=Hyderabad,IN&APPID=c63077b4593aed1e5101d3bb28ac6160'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print (data)
#print('Retrieved', len(data), 'characters')

try:

    js = json.loads(data)

except:
    js = None

temp = js["main"]["temp"]
loc = js["name"]

print("temperature:", temp)
print("location:", loc)
