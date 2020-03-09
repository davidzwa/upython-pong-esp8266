# blink

import network
from machine import Pin
from time import sleep
from slimDNS import SlimDNSServer
from uosc.client import Bundle, Client, create_message

led = Pin(2, Pin.OUT)
server_ip = "10.0.4.168"
client_ip = "10.0.4.1"

def await_connection():
    led = Pin(2, Pin.OUT)
    
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.1)
    
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

msg = "Hallo Jarno"
osc = Client(local_addr, 9001)
osc.send('/controls/frobnicator', 42, 3.1419, "spamm")
b = Bundle()
b.add(create_message("/foo", msg))
b.add(create_message("/spamm", 12345))
osc.send(b)
