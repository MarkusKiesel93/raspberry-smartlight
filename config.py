from pydantic import BaseSettings
from pathlib import Path
import RPi.GPIO as GPIO


class Config(BaseSettings):
    cors_allowed_origins: list = ['*']
    cors_allowed_methods: list = ['GET', 'POST']
    cors_allowed_headers: list = ['*']

    sheduler_user: str = 'pi'
    sheduler_comment: str = 'smartlight'
    sheduler_command: str = f'python3 {(Path("__file__").parent / "light_on.py").resolve()} &'

    gpio_mode = GPIO.BCM
    pin_bulb: int = 4
