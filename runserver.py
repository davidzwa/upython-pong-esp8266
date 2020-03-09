"""Small example OSC server

This program listens to several addresses, and prints some information about
received packets.
"""
import argparse
import math
import time
import pong

from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher
import asyncio

def filter_handler(address, *args):
    print(f"{address}: {args}")

async def loop():
    """Example main loop that only runs for 10 iterations before finishing"""
    pong.run_game()
    while 1: 
      for i in range(10):
          print(f"Loop {i}")
          await asyncio.sleep(1)

async def init_main(ip, port, dispatcher):
  server = AsyncIOOSCUDPServer((ip, port), dispatcher, asyncio.get_event_loop())
  print("Serving on {}".format(server))
  transport, protocol = await server.create_serve_endpoint()  # Create datagram endpoint and start serving

  await loop()  # Enter main loop of program

  transport.close()  # Clean up serve endpoint

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="0.0.0.0", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=5005, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = Dispatcher()
  dispatcher.map("/filter", filter_handler)

  asyncio.run(init_main(args.ip, args.port, dispatcher))
  