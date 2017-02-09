from machine import Pin
import time

p4 = Pin(4, Pin.OUT)

def toggle():
    global p4
    if p4.value():
        p4.low()
    else:
        p4.high()

for i range(0, 10):
    toggle()
    time.sleep(2)  # sleep two seconds
