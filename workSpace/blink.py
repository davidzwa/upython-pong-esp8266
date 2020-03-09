
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
print(local_addr)

if sta_if.isconnected():
    try:
        mdns = network.mDNS()
        mdns.start("mPy","MicroPython with mDNS")
        _ = mdns.addService('_ftp', '_tcp', 21, "MicroPython", {"board": "ESP32", "service": "mPy FTP File transfer", "passive": "True"})
        _ = mdns.addService('_telnet', '_tcp', 23, "MicroPython", {"board": "ESP32", "service": "mPy Telnet REPL"})
        _ = mdns.addService('_http', '_tcp', 80, "MicroPython", {"board": "ESP32", "service": "mPy Web server"})
    except Exception as e:
        print("mDNS not started", str(e))
        
server = SlimDNSServer(local_addr, "micropython")
response = server.advertise_hostname("servicename")
server.run_forever()

while (True):
    read_sockets = [server.sock]
    r = list(read_sockets)
    if server.sock in r:
        server.process_waiting_packets()




