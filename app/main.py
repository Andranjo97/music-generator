from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .config.env_manager import get_settings
from starlette.middleware.cors import CORSMiddleware

EnvManager = get_settings()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'] if EnvManager.is_dev() else [],
    allow_origin_regex=EnvManager.ALLOW_ORIGIN_REGEX,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
    expose_headers=['X-Total-Count']
)

handler = Mangum(app)
