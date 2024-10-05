
from pygame import mixer

mixer.init()

mixer.music.load("sounds1/757620__josefpres__piano-loops-095-efect-3-octave-long-loop-120-bpm.wav")

mixer.music.play()

while True:
	print("Press 'p' to pause, 'r' to resume") 
	print("Press 'e' to exit the program") 
	query = input("  ")

	if query == 'e':
		mixer.stop()
		break