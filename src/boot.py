# Complete project details at https://RandomNerdTutorials.com

import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()
import ujson
from server import start_server

try:
    config = open('config.json', 'r')
    config_str = config.read()
    config.close()
    print('Got settings:', config_str)
    config_json = ujson.loads(config_str)
    print('Got settings json:', config_json)
    if config_json['isConfigFound'] is True:
        print("yahoo")
        ssid = config_json['ssid']
        password = config_json['password']
        mqtt_server = config_json['ip']
        #EXAMPLE IP ADDRESS
        #mqtt_server = '192.168.1.144'
        client_id = ubinascii.hexlify(machine.unique_id())
        topic_sub = b'notification'
        topic_pub = b'hello'

        last_message = 0
        message_interval = 5
        counter = 0

        station = network.WLAN(network.STA_IF)

        station.active(True)
        station.connect(ssid, password)

        while station.isconnected() == False:
          pass

        print('Connection successful')
        print(station.ifconfig())
        
        
    else:
        print("ayyo")
        start_server()
        

except Exception as e:
    print(e)
    start_server()