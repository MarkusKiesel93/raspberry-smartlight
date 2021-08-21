import os
from pathlib import Path
from pydantic import BaseSettings


class Settings(BaseSettings):
    cors_allowed_origins: list = ['*']
    cors_allowed_methods: list = ['GET', 'POST']
    cors_allowed_headers: list = ['*']


settings = Settings()

