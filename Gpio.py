import RPi.GPIO as GPIO

from config import config

# todo change pritn to logging


class Gpio:
    def low(self, pin_number):
        try:
            GPIO.setmode(config.gpio_mode)
            GPIO.setwarnings(False)
            GPIO.setup(pin_number, GPIO.OUT)
            GPIO.output(pin_number, GPIO.LOW)
        except Exception as ex:
            print("turn on failed!")
            print(ex)

    def high(self, pin_number):
        try:
            GPIO.setmode(config.gpio_mode)
            GPIO.setwarnings(False)
            GPIO.setup(pin_number, GPIO.OUT)
            GPIO.output(pin_number, GPIO.HIGH)
        except Exception as ex:
            print("turn off failed!")
            print(ex)
        finally:
            GPIO.cleanup()
