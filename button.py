import RPi.GPIO as GPIO
import time
import subprocess
import os
import signal

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

alternate = False
while True:
	input_state = GPIO.input(5)
	if input_state == False:
		if alternate:
			p = subprocess.Popen("/home/pi/button/play.sh", shell=True, preexec_fn=os.setsid)
			print("play")
		else:	
			p = subprocess.Popen("/home/pi/button/pause.sh", shell=True, preexec_fn=os.setsid)
			print("pause")
		time.sleep(2)
		os.killpg(p.pid, signal.SIGTERM)
		alternate = not alternate
	time.sleep(0.2)
