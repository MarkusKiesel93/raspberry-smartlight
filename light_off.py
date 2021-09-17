import RPi.GPIO as GPIO
from config import config

# todo change print to logging

try:
    GPIO.setmode(config.gpio_mode)
    GPIO.setwarnings(False)
    GPIO.setup(config.pin_bulb, GPIO.OUT)
    GPIO.output(config.pin_bulb, GPIO.LOW)
except Exception as ex:
    print("turn off failed!")
    print(ex)
finally:
    GPIO.cleanup()