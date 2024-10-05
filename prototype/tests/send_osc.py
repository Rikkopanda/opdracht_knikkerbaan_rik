import os
import random
import pygame
from time import sleep
from pythonosc import udp_client


# Set up the OSC client to send messages to a specific address and port
client = udp_client.SimpleUDPClient("127.0.0.1", 8000)  # Replace with the receiver's IP address and port

# Send some example OSC messages
client.send_message("/filter/cutoff", 440)  # Send an integer value
# client.send_message("/synth/frequency", 123.456)  # Send a float value
# client.send_message("/greeting", "Hello, OSC!")  # Send a string value
client.send_message("/mixer_event/pause", "time for a break")  # Send a string value

print("OSC messages sent successfully!")