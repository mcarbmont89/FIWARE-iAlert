import requests
import json
import time
from time import sleep

url = 'localhost:1026/v1/updateContext'
payload = { "contextElements": [{"type": "iAlert","isPattern": "false","id": "000001","attributes": [{"name": "nombre","type": "value","value": "Juan Ramirez"},{"name" : "status", "type" : "value","value" : "off"}],"updateAction": "APPEND"}
headers = {'Content-Type' : 'application/json', 'Accept': 'application/json'}



def orden_boton():
	switch=0
	while True:
            switch=0
            time.sleep(60)
            switch=1
		    if switch==1: #If the button is pressed
                r = requests.post(url, data=json.dumps(payload),headers=json.dumps(headers)
try: 
    Thread.start_new_thread(orden_boton,())
except:
    print "Error"
while 1:
    pass

			