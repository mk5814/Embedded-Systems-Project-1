#This file is exectured on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import the libraries that are going to be used
import gc
import webrepl
import network
import machine
import time
from flicker import flickering

#create station and access point connections
webrepl.start()
gc.collect()
ap_if = network.WLAN(network.AP_IF)
#set up the access through the esp8266 wifi
ap_if.active(True)
sta_if =network.WLAN(network.STA_IF)
print('connecting to network...')
sta_if.active(True)
sta_if.connect('EEERover','exhibition')
while not sta_if.isconnected():
	pass
print('network config:', sta_if.ifconfig())
#else: print('false')

#print to screen

#check if the whole program runs
flickering()
