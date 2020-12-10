import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

gpio_red = 18
gpio_yellow = 23
gpio_green = 24

def colors(red=0, yellow=0, green=0):
	GPIO.setup(gpio_red, GPIO.OUT, initial = red)
	GPIO.setup(gpio_yellow, GPIO.OUT, initial = yellow)
	GPIO.setup(gpio_green, GPIO.OUT, initial = green)

colors(1,1,1)

try:
	while True:
		time.sleep(2)
		colors(0,0,1)
		time.sleep(.6)
		colors(0,1,0)
		time.sleep(1)
		colors(1,0,0)
		time.sleep(4)
except KeyboardInterrupt:
	GPIO.cleanup()
	print('done')

print('over')
