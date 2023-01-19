# import os
# import openai
# from dotenv import load_dotenv
# load_dotenv()

# openai.api_key = os.getenv("OPENAI_API_KEY")
# print(openai.Model.list())

from fastapi import FastAPI, HTTPException
from mangum import Mangum

app = FastAPI()

handler = Mangum(app)
