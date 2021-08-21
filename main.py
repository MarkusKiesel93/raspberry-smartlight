from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from config import settings


app = FastAPI(title=f'API - Smartlight')

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allowed_origins,
    allow_methods=settings.cors_allowed_methods,
    allow_headers=settings.cors_allowed_headers,
)


@app.get('/light/on/', status_code=status.HTTP_200_OK)
async def light_on():
    return 'Turn light on'


@app.get('/light/off/', status_code=status.HTTP_200_OK)
async def light_off():
    return 'Turn light off'


@app.post('/light/{hour}/{minute}', status_code=status.HTTP_200_OK)
async def light_at(hour: int, minute: int):
    return f'Turn light on at {hour}:{minute}'


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
