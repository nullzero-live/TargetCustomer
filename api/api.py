import os

import bcrypt
from dotenv import find_dotenv, load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import APIKeyHeader

from ..db import mongo_util

# Load environment variables
load_dotenv(find_dotenv())
# API Key for access
API_KEY_NAME = "api_key"
API_KEY_SECRET = os.getenv("API_KEY_SECRET")


# Initialize FastAPI
'''if API_KEY_NAME or API_KEY_SECRET == None:
    print("API Key is not set. Exiting...")
    exit()
else:'''
app = FastAPI()


# Function to get the API key from the request header
def get_api_key(api_key_header: str = Depends(APIKeyHeader(name=API_KEY_NAME))):
    if not bcrypt.checkpw(api_key_header.encode("utf-8"), API_KEY_SECRET.encode("utf-8")):
        raise HTTPException(status_code=400, detail="Invalid API Key")
    return api_key_header

@app.get("/retrieve_data/")
async def retrieve_data(api_key: str = Depends(get_api_key)):
    data = list(collection.find({}))
    return {"data": data}
