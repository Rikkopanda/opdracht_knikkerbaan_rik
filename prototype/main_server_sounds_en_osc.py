import os
import random
import pygame
from time import sleep
from pythonosc import udp_client
from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher
import asyncio
import threading
from functions.pygame_mixer_functions import setup_mixer_and_sounds, start_random_sound_with_timer
from functions.osc_server_functions import setup_dispatcher

# Use the setup_sounds function to initialize sounds
sounds1, sounds2 = setup_mixer_and_sounds()

# server = setup_dispatcher()

def filter_handler(address, *args):
    print(f"{address}: {args}")

dispatcher = Dispatcher()
dispatcher.map("/filter/cutoff", filter_handler)

ip = "127.0.0.1"
port = 8000
i = 0

async def loop():
	try:
		while True:
			print("Loop")
			await asyncio.sleep(0.2)
	except KeyboardInterrupt:
		print("main loop gestopt")

async def init_main():
    server = AsyncIOOSCUDPServer((ip, port), dispatcher, asyncio.get_event_loop())
    transport, protocol = await server.create_serve_endpoint()  # Create datagram endpoint and start serving

    await loop()  # Enter main loop of program

    transport.close()  # Clean up serve endpoint

start_random_sound_with_timer(sounds1, sounds2)

asyncio.run(init_main())


# try:
# 	while True:
# 		pass
# except KeyboardInterrupt:
# 	print("\nAfspelen gestopt.")
# finally:
pygame.mixer.quit()
