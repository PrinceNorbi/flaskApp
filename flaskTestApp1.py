#!/usr/bin/python3

#Needed for printing on console
#from __future__ import print_function # only in python 2.7
import sys

from flask import Flask
from flask import Response
from flask import jsonify
app=Flask(__name__)
app.debug=True
import random
import requests
import json
import collections
from collections import OrderedDict
import logging
import os.path
from flask import render_template

#from OpenSSL import SSL
#context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
#context.use_privatekey_file('/etc/letsencrypt/live/ad-astra.hu/privkey.pem')
#context.use_certificate_file('/etc/letsencrypt/live/ad-astra.hu/fullchain.pem')

if os.path.exists('/mnt/e/Google Drive/docs/linux/scripts/git/flaskApp/flaskTestApp.log'):
    LOG_FILENAME = '/mnt/e/Google Drive/docs/linux/scripts/git/flaskApp/flaskTestApp.log'
elif os.path.exists('/home/pi/git/flaskApp/flaskTestApp.log'):
    LOG_FILENAME = '/home/pi/git/flaskApp/flaskTestApp.log'
else:
    logging.error("Logfile is missing")

#file mode "a" for append, "w" for write
logging.basicConfig(format='%(asctime)s: %(levelname)s - %(message)s', filename=LOG_FILENAME, filemode='a',level=logging.INFO) 

import os
from flask import send_from_directory

@app.route("/")
def hello():
    #app.logger.info("Hello world logged")
    #logging.info("This is an info message")
    return render_template("menu.html")

#@app.route("/") #tried running bash command for dynamic menu items, problem with finding cat
#def hello():
#    bashCommand = '"/bin/cat flaskTestApp1.py | grep "^@app.route(\"/" | sed s/@app.route\(\"// | sed s/\"\)//"'
#    import subprocess
#    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
#    output, error = process.communicate()
#    return "$output"

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

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

@app.route("/btcCurrentToHuf")
def btcCurrentToHuf():
    r = requests.get('https://api.coinbase.com/v2/prices/spot?currency=HUF')
    parsed_json = (json.loads(r.text, object_pairs_hook=collections.OrderedDict))
    resp = Response(response=r, status=200, mimetype='application/json')
    print (jsonify(parsed_json))
    print((str(round((float(parsed_json['data']['amount'])*0.35508934)))), file=sys.stderr) #to also print it on console
    #getting data.amount value, multiply by the fraction I posess, convert to float, round it to whole, convert to string
    return(str(round((float(parsed_json['data']['amount'])*0.35508934)))) 
    #return jsonify(parsed_json) #output is fucking glorious as it should be

@app.route("/btc1ToHuf")
def btc1ToHuf():
    r = requests.get('https://api.coinbase.com/v2/prices/spot?currency=HUF')
    parsed_json = (json.loads(r.text, object_pairs_hook=collections.OrderedDict))
    resp = Response(response=r, status=200, mimetype='application/json')
    #print (jsonify(parsed_json))
    return(str(round((float(parsed_json['data']['amount'])))))
    #return jsonify(parsed_json) #output is fucking glorious as it should be

@app.route("/daysUntilNice")
def daysUntilNice():
    return render_template("countdown.html")
