#!/usr/bin/python3
from flask import Flask
from flask import Response
from flask import jsonify
app=Flask(__name__)
app.debug=True
import random
import requests
import json

@app.route("/")
def hello():
    return "Hello world\n"

@app.route("/random")
def randomGen():
    return str(random.randint(1,100))+"\n"

@app.route("/lightsOn")
def lightSwitchOn():
    dataOn = '{"on":true}'
    response = requests.put('http://192.168.0.178/api/hsZenWXoKuMZc6QsR2lyFIBcn3RmbCv-VM6Pp9-4/lights/2/state', data=dataOn)
    return "Lights are turned on now."

@app.route("/lightsOff")
def lightSwitchOff():
    dataOff = '{"on":false}'
    response = requests.put('http://192.168.0.178/api/hsZenWXoKuMZc6QsR2lyFIBcn3RmbCv-VM6Pp9-4/lights/2/state', data=dataOff)
    return "Lights are turned off now."

@app.route("/lightsStatus")
def lightSwitchStatus4():
    r = requests.get('http://192.168.0.178/api/hsZenWXoKuMZc6QsR2lyFIBcn3RmbCv-VM6Pp9-4/lights/2')
    parsed_json = (json.loads(r.text))
    resp = Response(response=r, status=200, mimetype='application/json')
    print (jsonify(parsed_json))
    return jsonify(parsed_json) #output is fucking glorious as it should be
