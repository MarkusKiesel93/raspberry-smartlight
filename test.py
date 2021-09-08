import RPi.GPIO as GPIO
from time import sleep

pin_bulb = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_bulb, GPIO.OUT)
GPIO.output(pin_bulb, GPIO.LOW)
sleep(3)
GPIO.output(pin_bulb, GPIO.LOW)
GPIO.cleanup()