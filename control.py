from Gpio import Gpio
from sheduler import Sheduler
from config import config

gpio = Gpio()


def light_on():
    gpio.on(config.pin_bulb)


def light_off():
    gpio.off(config.pin_bulb)
    Sheduler().reset()


def ambient_light_on():
    gpio.on(config.pin_ambient)


def ambient_light_off():
    gpio.off(config.pin_ambient)
