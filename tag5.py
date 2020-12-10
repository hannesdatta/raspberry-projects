import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

seg = 13

zif= [16, 12, 7, 6]

def onoff(pin, state):
	GPIO.setup(pin, GPIO.OUT, initial=state)

onoff(13,1)
for z in zif: onoff(z, 1)

try:
	while True:
		for z in zif:
			onoff(z,0)
			time.sleep(.2)
			onoff(z,1)
except KeyboardInterrupt:
	time.sleep(1)
	GPIO.cleanup()
