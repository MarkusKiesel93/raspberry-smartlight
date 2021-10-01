from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.config import config
import app.control as control
from app.sheduler import Sheduler


app = FastAPI(title='API - Smartlight')


app.add_middleware(
    CORSMiddleware,
    allow_origins=config.cors_allowed_origins,
    allow_methods=config.cors_allowed_methods,
    allow_headers=config.cors_allowed_headers,
)


@app.get('/light/on/', status_code=status.HTTP_200_OK)
async def light_on():
    control.light_on()


@app.get('/light/off/', status_code=status.HTTP_200_OK)
async def light_off():
    control.light_off()


@app.get('/ambient-light/on/', status_code=status.HTTP_200_OK)
async def abient_light_on():
    control.ambient_light_on()


@app.get('/ambient-light/off/', status_code=status.HTTP_200_OK)
async def ambient_light_off():
    control.ambient_light_off()


@app.post('/light/{hour}/{minute}', status_code=status.HTTP_200_OK)
async def wakeup_light(hour: int, minute: int):
    if hour < 0 or hour > 12 or minute < 0 or minute > 60:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Not a correct time.'
        )
    Sheduler().set(hour, minute)