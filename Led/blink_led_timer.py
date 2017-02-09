from machine import Pin, Timer

p4 = Pin(4, Pin.OUT)
timer = Timer(-1)

def toggle():
    global p4
    if p4.value():
        p4.low()
    else:
        p4.high()

# toggles the led every two seconds
timer.init(period=2000, mode=Timer.PERIODIC, callback=lambda t: toggle())
