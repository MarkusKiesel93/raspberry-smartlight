import RPi.GPIO as GPIO

from config import settings


class Light:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

    def on(self):
        try:
            GPIO.setup(settings.pin_bulb, GPIO.OUT)
            GPIO.output(settings.pin_bulb, GPIO.HIGH)
        except Exception as ex:
            print("turn on failed!")
            print(ex)

    def off(self):
        try:
            GPIO.setwarnings(False)
            GPIO.setup(settings.pin_bulb, GPIO.OUT)
            GPIO.output(settings.pin_bulb, GPIO.LOW)
        except Exception as ex:
            print("turn off failed!")
            print(ex)
        finally:
            GPIO.cleanup()


if __name__ == '__main__':
    light = Light()
    light.on()