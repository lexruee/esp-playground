from machine import Pin
import time

led = Pin(14, Pin.OUT)

def toggle():
    global led
    if led.value():
        led.low()
    else:
        led.high()

for i in range(0, 10):
    toggle()
    time.sleep(2)  # sleep two seconds
