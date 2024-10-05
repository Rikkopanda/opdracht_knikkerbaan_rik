
from pythonosc import dispatcher
from pythonosc import osc_server
from time import sleep

from functions.pygame_mixer_functions import pauze_random_sounds

def print_handler(address, *args):
    print(f"Received message: {address} - {args}")

def pauze_handler(address, *args):
	print(f"Received message: {address} - {args}")
	pauze_random_sounds()

def setup_dispatcher():
	# Set up the dispatcher to handle incoming messages
	dispatcher = dispatcher.Dispatcher()
	dispatcher.map("/filter/cutoff", print_handler)  # Handle the /filter/cutoff address
	dispatcher.map("/synth/frequency", print_handler)  # Handle the /filter/cutoff address
	dispatcher.map("/greeting", print_handler)  # Handle the /filter/cutoff address
	dispatcher.map("/mixer_events/pauze", pauze_handler)  # Handle the /filter/cutoff address

 	# Set up the server
	server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", 8000), dispatcher)
	return  server

# concurrent mode so that server doesn't block main program
def setup_dispatcher_concurrent():
	# Set up the dispatcher to handle incoming messages
	dispatcher = dispatcher.Dispatcher()
	dispatcher.map("/filter/cutoff", print_handler)  # Handle the /filter/cutoff address
	dispatcher.map("/synth/frequency", print_handler)  # Handle the /filter/cutoff address
	dispatcher.map("/greeting", print_handler)  # Handle the /filter/cutoff address
	dispatcher.map("/mixer_events/pauze", pauze_handler)  # Handle the /filter/cutoff address

 	# Set up the server
	server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", 8000), dispatcher)
	return  server