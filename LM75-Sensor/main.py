from machine import I2C, Pin, Timer
from lm75 import LM75

i2c = I2C(sda=Pin(4), scl=Pin(5))
lm = LM75(i2c=i2c)
timer = Timer(-1)


def print_temp(lm):
    print(lm.read_temperature())

timer.init(period=4000, mode=Timer.PERIODIC, callback=lambda _: print_temp(lm))