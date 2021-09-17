import RPi.GPIO as GPIO
from config import config

# todo change pritn to logging

try:
    GPIO.setmode(config.gpio_mode)
    GPIO.setup(config.pin_bulb, GPIO.OUT)
    GPIO.output(config.pin_bulb, GPIO.HIGH)
except Exception as ex:
    print("turn on failed!")
    print(ex)
