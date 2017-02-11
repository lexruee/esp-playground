from machine import Pin
import time


class MyPin(Pin):

    def toggle(self):
        self.value(not self.value())

led = MyPin(14, Pin.OUT)

while True:
    led.toggle()
    time.sleep(2)  # sleep two seconds
