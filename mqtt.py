import json
from umqtt.simple import MQTTClient

client = MQTTClient('Trezeguet_id','192.168.0.10')

def mqtt_print(connected, city, choice, direction, degrees, t):
    
    #use a variable in json format to upload the processed data
    if choice == 'compass':
        payload = json.dumps([{'mode: ':choice}, {'desired direction: ':direction}, {'you want to face: ':city}, {'your bearing from north is = ':degrees}])
    else:
        payload = json.dumps([{'mode: ':choice}, {'origin: ':city}, {'desired direction: ':direction}, {'your bearing from north is = ':degrees}])

    #ensure that client.connet() only happens once
    if connected:
        client.connect()
    if t == 9:
        client.publish('esys/Trezeguet/',bytes(payload,'utf-8'))
    print(degrees)
