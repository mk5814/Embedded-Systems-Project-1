import machine
import time
import math
import json
import sys
from machine import Pin, I2C
from read import cont_read, buzzer
from bearings2 import bearing
from umqtt.simple import MQTTClient
from flicker import flickering
from nsew import pointing
from mqtt import mqtt_print

#create a LUT containing cities and their respective bearings from Mecca
lookup = {'london': 121, 'beijing': 285, 'new york': 72, 'sao paulo': 89, 'cape town': 47, 'paris': 120, 'prague': 133}

#variable ensures that client.connect() only occurs once to prevent memory errors
connected = True

#set a counter to print on the MQTT screen every 1 second
t = 0

#set the interface to the user's input
purpose = input('would you like to use this device as a prayer mat? y/n \n')
#flag is a variable used to stay in the while loop until a valid city/bearing is input
flag = True
if purpose == 'y':
    #prayer mat option is set
    while flag:
        city = (input('please enter desired city: \n')).lower()
        if city in lookup:
            direction = lookup[city]
            flag = False
        else:
            print('city not found')
    choice = 'prayer mat'
else:
    #custom bearing is set
    while flag:
        flag = False
        try:
            direction = float(input('please enter desired bearing: \n'))
        except ValueError:
            print('not a number')
            flag = True
    choice = 'compass'
    #standardise the bearing to a value between 0 and 360
    if direction < 0:
        while direction < 0:
            direction += 360
    elif direction >= 360:
        while direction >= 360:
            direction -= 360
    city = pointing(direction)
    
#print desired bearing
print(direction)

time.sleep_ms(5000)

#infinite loop that reads the data from the magnetometer, prints the data and sends input to the other sensors accordingly
while True:
    degrees = cont_read()
    mqtt_print(connected, city, choice, direction, degrees, t)
    time.sleep_ms(100)
    buzzer(degrees, direction)
    #client.connect() will not happen again
    connected = False
    t = t + 1
    #printing only happens every 10 cycles (1000 ms)
    if t == 10:
        t = 0

#check if the whole main program runs; if the light flashes, there is an error
flickering()
