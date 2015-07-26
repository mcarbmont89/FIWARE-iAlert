import time
import RPi.GPIO as GPIO
from time import sleep
import requests
import json
GPIO.setwarnings(False)# Evita los warnings
GPIO.setmode(GPIO.BCM)

url = 'localhost:1026/v1/subscribeContext'
payload = {"entities": [{"type": "","isPattern": "false","id": "Victima-100900800901"}],"attributes": ["nombre"],"reference": "http://localhost:1028/accumulate","duration": "P1M","notifyConditions": [{"type": "ONCHANGE","condValues": ["status"]}],"throttling": "PT5S"}
headers = {'Content-Type' : 'application/json', 'Accept': 'application/json'}

def orden_boton():
	switch=GPIO.input(23)
	while True:
		switch=GPIO.input(23)
		if switch==GPIO.HIGH: #If the button is pressed
            r = requests.post(url, data=json.dumps(payload), headers=json.dumps(headers))
try: 
    Thread.start_new_thread(orden_boton,())
except:
    print "Error"
while 1:
    pass