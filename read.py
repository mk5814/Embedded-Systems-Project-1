import machine
import time
import math
from machine import Pin, I2C
from bearings2 import bearing

def cont_read():
    
    #create an instance of the I2C class,ArithmeticError initialize pins 4, 5
    i2c = machine.I2C(scl=Pin(5), sda=Pin(4), freq=100000)
    
    #from datasheet initialize configuration registers
    i2c.writeto_mem(0x1E, 0x00, b'\0x70')
    i2c.writeto_mem(0x1E, 0x01, b'\0xA0')
    i2c.writeto_mem(0x1E, 0x02, b'\0x00')
    time.sleep_ms(6)
    
    #start reading values from the output registers
    data = i2c.readfrom_mem(0x1E, 0x03, 6)
    
    #convert the 6 8-bit numbers into 3 16-bit values and store as unsigned integers
    X = data[0]*256 +data[1]
    Z = data[2]*256 +data[3]
    Y = data[4]*256 +data[5]
    
    #convert the unsigned values to signed for correct operation from the datasheet
    if X > 2047:
        X -= 65536
    if Z > 2047:
        Z -= 65536
    if Y > 2047:
        Y -= 65536

    #uses the axes X and Y to find the bearing
    degrees = bearing(X, Y)
    if degrees < 0:
        degrees += 360
    return degrees

def buzzer(degrees, direction):

    #p12 is right buzzer, p13 is left buzzer, and p15 is LED
    p12 = Pin(12, Pin.OUT)
    p13 = Pin(13, Pin.OUT)
    p15 = Pin(15, Pin.OUT)
    p12.low()
    p13.low()
    p15.low()
    
    #set a tolerance for the desired bearing
    right_bound = 22.5
    left_bound = 337.5

    #set a tolerance for the bearing behind desired bearing
    behind_left = 202.5
    behind_right = 157.5

    #subtract desired bearing to standardise the function
    degrees = degrees - direction
    
    if degrees < 0:
        degrees = degrees + 360

    if degrees < behind_right and degrees >= right_bound: #only left buzzer on, LED off
        p12.low()
        p13.high()
        p15.low()
    elif degrees >= behind_left and degrees < left_bound: #only right buzzer on, LED off
        p12.high()
        p13.low()
        p15.low()
    elif degrees >= behind_right and degrees < behind_left: #both buzzers on, LED off
        p12.high()
        p13.high()
        p15.low()
    else: #degrees >= left_bound or degrees < right_bound: #both buzzers off, LED on
        p12.low()
        p13.low()
        p15.high()
