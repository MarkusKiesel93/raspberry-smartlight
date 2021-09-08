import RPi.GPIO as GPIO
from time import sleep


from config import Config


class Light:

    def __init__(self):
        pass

    def test(self):
        GPIO.setmode(Config.gpio_mode)
        GPIO.setup(Config.pin_bulb, GPIO.OUT)
        GPIO.output(Config.pin_bulb, GPIO.LOW)
        sleep(3)
        GPIO.output(Config.pin_bulb, GPIO.LOW)
        GPIO.cleanup()

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
    light.test()