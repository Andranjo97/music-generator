from fastapi import FastAPI, HTTPException
from mangum import Mangum

app = FastAPI()

handler = Mangum(app)
