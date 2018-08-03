

import requests
 
# api-endpoint     //sending a request through this url
URL = "http://api.openweathermap.org/data/2.5/weather?q=Hyderabad,IN&APPID=c63077b4593aed1e5101d3bb28ac6160"
 
location = "Hyderabad"     # location given here
 
# defining a params dictionary for the parameters to be sent to the API
PARAMS = {'address':location}  



# sending get request and saving the response from server as  response object
r = requests.get(url = URL, params = PARAMS)     #two args r url and parameters dictionery 
#print (r.text)
print("\n")




# extracting data in json format
data = r.json()
print (data)
print('Retrieved', len(data), 'characters')
 
 
