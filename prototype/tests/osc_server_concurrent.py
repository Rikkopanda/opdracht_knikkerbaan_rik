from pythonosc import dispatcher
from pythonosc import osc_server
from time import sleep
import os
import random
import pygame
from time import sleep
from pythonosc import udp_client
from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher
import asyncio
import threading
from functools import partial

def filter_handler(address, *args):
    print(f"{address}: {args}")

dispatcher = Dispatcher()
dispatcher.map("/filter/cutoff", filter_handler)

ip = "127.0.0.1"
port = 8000
i = 0

async def loop():
	"""Example main loop that only runs for 10 iterations before finishing"""
	try:
		while True:
			print("Loop")
			await asyncio.sleep(1)
			# i = i + 1
	except KeyboardInterrupt:
		print("main loop gestopt")

async def init_main():
    server = AsyncIOOSCUDPServer((ip, port), dispatcher, asyncio.get_event_loop())
    transport, protocol = await server.create_serve_endpoint()  # Create datagram endpoint and start serving

    await loop()  # Enter main loop of program

    transport.close()  # Clean up serve endpoint

asyncio.run(init_main())
