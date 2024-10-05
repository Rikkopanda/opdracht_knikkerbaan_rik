from pythonosc import dispatcher
from pythonosc import osc_server
from time import sleep

def print_handler(address, *args):
    print(f"Received message: {address} - {args}")

def setup_dispatcher():
	# Set up the dispatcher to handle incoming messages
	dispatcher = dispatcher.Dispatcher()
	dispatcher.map("/filter/cutoff", print_handler)  # Handle the /filter/cutoff address
	dispatcher.map("/synth/frequency", print_handler)  # Handle the /filter/cutoff address
	dispatcher.map("/greeting", print_handler)  # Handle the /filter/cutoff address
	# Set up the server
	server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", 8000), dispatcher)
	return  server


server = setup_dispatcher()



print("Serving on {}".format(server.server_address))
try:
	server.serve_forever()  # Start the server to listen for incoming OSC messages
except KeyboardInterrupt:
	print("server gestopt")

while True:
    print("program loop")
    sleep(1)
