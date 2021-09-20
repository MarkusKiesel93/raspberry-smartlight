from Gpio import Gpio
from sheduler import Sheduler
from config import config

gpio = Gpio()


def light_on():
    gpio.low(config.pin_bulb)


def light_off():
    gpio.high(config.pin_bulb)
    Sheduler().reset()


def ambient_light_on():
    gpio.high(config.pin_ambient)


def ambient_light_off():
    gpio.low(config.pin_ambient)
