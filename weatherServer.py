
from flask import Flask, jsonify, request, session, abort, flash, redirect
from flask import render_template
from classCode import Example
import json

app = Flask(__name__)


@app.route("/", methods=['GET'])     
def hello():
    obj = Example()
    #print (obj.myfunc())
    print("\n")
    print ("naveen")
    s = obj.myfunc()
    print (s)           #prints json data in terminal
    print("\n")
    
    print("converting from json to python")
    print("\n")

    coord_longitude = s['coord']['lon']
    coord_latitude = s['coord']['lat']
    
    main_temp = s['main']['temp']
    main_pressure = s['main']['temp']
    main_humidity = s['main']['temp']




    print (coord_longitude)


    '''jp = json.parse(s)
    coordinates = jp.coord
    print(coordinates)'''

    # print to screen
    

    '''jp = json.loads(json_encoded)            #converts json to python
    print (jp['temp'])
    print (jp['pressure']'''

    return ("hello world")


if __name__ == '__main__':
    #print ("success")
    app.run(debug=True)
    print ("success")