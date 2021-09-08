import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(Config.gpio_mode)
GPIO.setup(Config.pin_bulb, GPIO.OUT)
GPIO.output(Config.pin_bulb, GPIO.LOW)
sleep(3)
GPIO.output(Config.pin_bulb, GPIO.LOW)
GPIO.cleanup()