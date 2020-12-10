import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

seg = [21,13,26]

for s in seg:
	print(s)
	GPIO.setup(seg, GPIO.OUT, initial=1)

time.sleep(5)

GPIO.cleanup()
