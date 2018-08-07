from flask import Flask, jsonify, request, session, abort, flash, redirect
from flask import render_template
from classCode import Example
from datetime import datetime
import json
app = Flask(__name__)

obj = Example()

@app.route("/", methods=['GET'])     
def hello():
    #obj = Example()
    #print (obj.myfunc())
    print("\n")
    print ("naveen")
    s = obj.myfunc()
    print (s)           #prints json data in terminal
    print("\n")
    print("converting from json to python")
    print("\n")
    location = s['name']
    print (location)
    coord_longitude = s['coord']['lon']
    print (coord_longitude)
    coord_latitude = s['coord']['lat']
    print (coord_latitude)
    print("\n")
    print("weather details")
    for w in s['weather']:   #to parse a json array
        w_id = w['id']
        print ('weather-id :', w_id)
        w_main = w['main']
        print ('weather-main :', w_main)
        w_description = w['description']
        print ('weather-description :', w_description)
        w_icon = w['icon']
        print ('weather-icon :', w_icon)
    
    b = s['base']
    print('base : ', b)
           
    print("main details")
    m_temp = s['main']['temp']
    print ('temperature : ', m_temp)
    m_pressure = s['main']['pressure']
    print ('pressure : ', m_pressure)
    m_humidity = s['main']['humidity']
    print ('humidity : ', m_humidity)
    m_temp_min = s['main']['temp_min']
    print ('min temperature : ', m_temp_min)
    m_temp_max = s['main']['temp_max']
    print ('max temperature : ', m_temp_max)
    country = s['sys']['country']
    vis = s['visibility']
    print('visibility : ', vis)
    print("\n")
    print("wind details")
    w_speed = s['wind']['speed']
    print("wind speed: ",w_speed)
    w_deg = s['wind']['deg']
    print("wind degrees: ",w_deg)
    print ('\n')
    print("cloud details")
    cloud = s['clouds']['all']
    print('all : ',cloud) 
    print('\n')   
    d_t = s['dt']
    print('dt : ', d_t)    
    print('sys details')
    s_type = s['sys']['type'] 
    print('type : ', s_type)
    s_id = s['sys']['id']
    print('id : ', s_id)
    s_msg = s['sys']['message']
    print('message : ', s_msg)
    s_country = s['sys']['country']
    print('country : ', s_country)
    sun_rise = s['sys']['sunrise']
    print('sunrise : ',sun_rise)
    s_sunrise = datetime.fromtimestamp(sun_rise) 
    print('SUNRISE : ',s_sunrise)
    sun_set = s['sys']['sunset']
    print('sunset : ',sun_set)
    s_sunset = datetime.fromtimestamp(sun_set) 
    print('SUNSET : ',s_sunset)   
    print()
    print("\n")
    iden = s['id']
    print("id : ",iden)
    code = s['cod']
    print("cod : ",code)
    return ("hello world")

#fake api's code

@app.route("/users", methods=['GET'])   
def fake():
    fake_data = obj.users()
    #print (fake_data)
    for f in fake_data:
        f_name = f['name']
        f_id = f['id']
        f_city = f['address']['city']
        f_lat = f['address']['geo']['lat']
        f_long = f['address']['geo']['lng']
        f_mob = f['phone']
        f_company = f['company']['name']
        #print('\n')
        print ("name : ",f_name)        
        print ("id : ",f_id)
        print ('company name : ',f_company)
        print ('city : ',f_city)
        print ("latitude : ",f_lat)
        print ("longitude : ",f_long)
        print ('phone : ',f_mob)
        print('\n')
    return ("users world")

@app.route("/opensource", methods=['GET'])   
def os():
    print ("Inside dummies")

    with open('weather.json') as json_file:  #read
        d = json.load(json_file)
        print("1234")
        print(d)
        d_id = d['id']
        d_type = d["type"]
        d_name = d["name"]
        d_ppu = d["ppu"]             
        #batters = d['batters']
        #print (batters) 
        
        print("id :",d_id)
        print("type :",d_type)
        print("name :",d_name)
        print("ppu :",d_ppu)

        for b in d['batters']['batter']:    #prints inside batter array
            #print("for loop")
            print ("id : ",b['id'])
            print ("type : ",b['type'])

        for t in topping:
            print ("id : ",top['id'])

    
        
    return ("open source.adobe")
    #return jsonify(topic=d["Topic"], msg=d["Message"])    #returns to html in json format    
    
    
if __name__ == '__main__':
    #print ("success")
    app.run(debug=True)
    print ("success")






