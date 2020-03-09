
# blink

import network
from machine import Pin
from time import sleep
from slimDNS import SlimDNSServer
# from utils import await_connection


led = Pin(2, Pin.OUT)

def await_connection():
    led = Pin(2, Pin.OUT)
    
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.1)
    # print("Hello world!")
    
sta_if = network.WLAN(network.STA_IF)

sta_if.active(True) # Dont spawn own WiFi
sta_if.connect('DS4_TROPEN', 'groen333')

while not sta_if.isconnected():
  await_connection()
  sleep(1)
  print("Awaiting wifi connection.")

ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)
print("Connected to DS4_TROPEN (wifi AP now disabled):")
print(sta_if.ifconfig())
  
local_addr = sta_if.ifconfig()[0]
print("My IP:", local_addr)



