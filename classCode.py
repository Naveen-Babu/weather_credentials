
import requests,json


class Example:
    def myfunc(self):  #self is used to access class variables
            
        URL = "http://api.openweathermap.org/data/2.5/weather?q=Hyderabad,IN&APPID=c63077b4593aed1e5101d3bb28ac6160"
        location = "Hyderabad"     # location given here
        PARAMS = {'address':location}  
       
        # sending get request and saving the response from server as  response object
        r = requests.get(url = URL, params = PARAMS)     #two args r url and parameters dictionery 
        print (r.url)
        print("\n")
       
        #extracting data in json format
        data = r.json()
        return (data)


#fake apis

    def users(self):
        URL = "https://jsonplaceholder.typicode.com/users"
        req = requests.get(url = URL)   
        #print (req)
        user_data = req.json()
        #print(user_data)
        return (user_data)

b = Example()
print(b.users())

        











