import time
import RPi.GPIO as GPIO
from time import sleep
import requests
import json
GPIO.setwarnings(False)# Evita los warnings
GPIO.setmode(GPIO.BCM)

url = 'localhost:1026/v1/updateContext'
payload = { "contextElements": [{"type": "iAlert","isPattern": "false","id": "000001","attributes": [{"name": "nombre","type": "value","value": "Juan Ramirez"},{"name" : "status", "type" : "value","value" : "off"}],"updateAction": "APPEND"}
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