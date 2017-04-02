import RPi.GPIO as GPIO
import time
import subprocess
import os
import signal

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

alternate = False


# scan for the chromecast and save it's logical address
with open("/home/pi/chromecast-button/device", "w") as f:
  device = 4
  scan = subprocess.Popen("echo scan | cec-client -s -d 1", stdout=subprocess.PIPE, shell=True)
  for line in scan.stdout:
     line = line.lower()
     if line.find("device #") > -1:
          info = line.split()
          device = info[1][1:-1]
     if line.find("chromecast") > -1:
          print(str(device))
          break
  f.write(device)
  f.close

while True:
	input_state = GPIO.input(5)
	if input_state == False:
		if alternate:
			p = subprocess.Popen("/home/pi/chromecast-button/play.sh", shell=True, preexec_fn=os.setsid)
			print("play")
		else:	
			p = subprocess.Popen("/home/pi/chromecast-button/pause.sh", shell=True, preexec_fn=os.setsid)
			print("pause")
		time.sleep(2)
		os.killpg(p.pid, signal.SIGTERM)
		alternate = not alternate
	time.sleep(0.2)
