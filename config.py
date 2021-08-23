from pydantic import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    cors_allowed_origins: list = ['*']
    cors_allowed_methods: list = ['GET', 'POST']
    cors_allowed_headers: list = ['*']

    sheduler_user: str = 'pi'
    sheduler_comment: str = 'smartlight'
    sheduler_command: str = f'python {(Path("__file__").parent / "light.py").resolve()} &'

    pin_bulb: int = 4


settings = Settings()
