import RPi.GPIO as GPIO
from config import Config

# todo change pritn to logging

try:
    GPIO.setmode(Config.gpio_mode)
    GPIO.setup(Config.pin_bulb, GPIO.OUT)
    GPIO.output(Config.pin_bulb, GPIO.LOW)
except Exception as ex:
    print("turn on failed!")
    print(ex)
