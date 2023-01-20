from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .config.env_manager import get_settings
from .config.routes_registerer import register_routers
from starlette.middleware.cors import CORSMiddleware

EnvManager = get_settings()

app = FastAPI(title='Music Generator')
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'] if EnvManager.is_dev() else [],
    allow_origin_regex=EnvManager.ALLOW_ORIGIN_REGEX,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
    expose_headers=['X-Total-Count']
)

register_routers(app=app, routers_path='app.routers', stg_name='api')

@app.get("/")
async def get():
    return {"app": "Music Generator", "version": "0.0.1", "backend": "lambda"}

handler = Mangum(app)
