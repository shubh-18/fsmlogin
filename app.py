#!/usr/bin/env python

import urllib
import json
import os
import subprocess
import re

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    	req = request.get_json(silent=True, force=True)

    	print("Request:")
    	print(json.dumps(req, indent=4))

    	res = makeWebhookResult(req)

    	res = json.dumps(res, indent=4)
    	print(res)
    	r = make_response(res)
    	r.headers['Content-Type'] = 'application/json'
    	return r

def makeWebhookResult(req):
    	if req.get("result").get("action") != "user.id":
		return{}
    	result = req.get("result")
    	parameters = result.get("parameters")
    	id1 = parameters.get("user-id")
    	pass1 = parameters.get("password")
    	cost = {'Suraj':100, 'Shubham':200, 'Raju':300, 'Yash':400, 'Ravi':500}
	ip={'Suraj':'google.com', 'Shubham':'youtube.com', 'Raju':'facebook.com', 'Yash':'yahoo.com', 'Ravi':500}
    	if(str(cost[id1])==pass1):
        	speech = id1 + ". You are Suceesfully login. Do you have any problem with our product."
		myUrl = str(ip[id1])
		ping=subprocess.Popen(["ping", myUrl], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, error=ping.communicate()
		out=str(out)
    	else:
        	speech = "Wrong credential"

    	print("Response:")
    	print(speech)
    	print(out)

    	return {
        	"speech": speech,
        	"displayText": speech,
        	"out": out,
		"displayText": out,
        #"data": {},
        # "contextOut": [],
        	"source": "apiai-onlinestore-shipping"
    	}


if __name__ == '__main__':
    	port = int(os.getenv('PORT', 5000))

    	print "Starting app on port %d" % port

    	app.run(debug=True, port=port, host='0.0.0.0')
