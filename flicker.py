import machine
import time

def flickering():
    pin = machine.Pin(2, machine.Pin.OUT)
    time.sleep_ms(250)
    pin.high()
    time.sleep_ms(250)
