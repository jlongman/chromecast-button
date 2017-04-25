import RPi.GPIO as GPIO
import time
import subprocess
import os
import signal

pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

alternate = False


def scan():
  scan = subprocess.Popen("echo scan | cec-client -s -d 1", stdout=subprocess.PIPE, shell=True)
  device = -1
  found_device = device
  for line in scan.stdout:
     line = line.lower()
     if line.find("device #") > -1:
          info = line.split()
          found_device = info[1][1:-1]
     if line.find("chromecast") > -1:
          device = found_device
          break
  return device

# scan for the chromecast and save it's logical address
with open("/home/pi/chromecast-button/device", "w") as f:
  device = "4"
  try:
     print("Scanning for ChromeCast...")
     found_device = scan()
     if (found_device < 0):
        print("Chromecast not active, retry")
        time.sleep(1)
        found_device = scan()
        if found_device < 0:
           print("Chromecast not active, use 4")
           found_device = 4
  except:
     print("Chromecast error, use 4")
     found_device = 4
  device = str(found_device)
  print("Using " + device)
  f.write(device)
  f.close

while True:
	input_state = GPIO.input(pin)
	if input_state == False:
		if alternate:
			p = subprocess.Popen("/home/pi/chromecast-button/play.sh", shell=True, preexec_fn=os.setsid)
#			print("play")
		else:	
			p = subprocess.Popen("/home/pi/chromecast-button/pause.sh", shell=True, preexec_fn=os.setsid)
#			print("pause")
		time.sleep(2)
		os.killpg(p.pid, signal.SIGTERM)
		alternate = not alternate
	time.sleep(0.2)
