from machine import Pin
from time import sleep_ms
from uosc.client import Client


UPDATE_DELAY = const(50)
OSC_SERVER = '10.0.4.197'
OSC_PORT = const(5005)
OSC_TOPIC = '/filter'


def main():
    osc = Client(OSC_SERVER, OSC_PORT)
    
    try:
        while True:
            osc.send(OSC_TOPIC, "Filtered", "Data")
            sleep_ms(UPDATE_DELAY)
    except Exception as exc:
        print(exc)


if __name__ == '__main__':
    main()

