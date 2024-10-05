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


# Function to initialize Pygame and load sounds
def setup_mixer_and_sounds():
    # Initialize Pygame mixer
    pygame.mixer.init()

    # Define sound directories
    sounds1_path = 'sounds1'
    sounds2_path = 'sounds2'

    # Load all sound files from the directories
    sounds1 = [os.path.join(sounds1_path, f) for f in os.listdir(sounds1_path) if f.endswith('.wav')]
    sounds2 = [os.path.join(sounds2_path, f) for f in os.listdir(sounds2_path) if f.endswith('.wav')]

    # Check if sounds were loaded successfully
    if not sounds1 or not sounds2:
        print("Error: Geluidsbestanden niet gevonden in een van de mappen.")
        exit()
    # Return the loaded sounds and paths
    return sounds1, sounds2

def start_random_sound_with_timer(sounds1, sounds2):
	"""Speel twee willekeurige geluiden, een uit elk mapje."""
	sound1 = random.choice(sounds1)
	sound2 = random.choice(sounds2)
	print("sound1:\n")
	print(sound1)
	print("sound2:\n")
	print(sound2)
	# Zorg ervoor dat ze niet hetzelfde geluid kiezen
	while sound1 == sound2:
		sound2 = random.choice(sounds2)

	# Geluiden laden en afspelen
	pygame.mixer.Sound(sound1).play()
	pygame.mixer.Sound(sound2).play()
	play_sound_with_args = partial(start_random_sound_with_timer, sounds1, sounds2)  # Create a function with bound arguments
	threading.Timer(3, play_sound_with_args).start()
 
def pauze_random_sounds():
	pygame.mixer.pause()