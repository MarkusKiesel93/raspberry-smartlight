import RPi.GPIO as GPIO
from config import Config

# todo change print to logging

try:
    GPIO.setmode(Config.gpio_mode)
    GPIO.setwarnings(False)
    GPIO.setup(Config.pin_bulb, GPIO.OUT)
    GPIO.output(Config.pin_bulb, GPIO.HIGH)
except Exception as ex:
    print("turn off failed!")
    print(ex)
finally:
    GPIO.cleanup()