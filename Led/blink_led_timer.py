from machine import Pin, Timer

led = Pin(14, Pin.OUT)
timer = Timer(-1)

def toggle():
    global led
    if led.value():
        led.low()
    else:
        led.high()

# toggles the led every two seconds
timer.init(period=2000, mode=Timer.PERIODIC, callback=lambda t: toggle())
