# blink

from machine import Pin
from time import sleep
led = Pin(13, Pin.OUT)
while True:
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.1)
    print("Hello world!")

