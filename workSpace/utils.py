from machine import Pin
from time import sleep

def await_connection():
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.1)
    # print("Hello world!")
