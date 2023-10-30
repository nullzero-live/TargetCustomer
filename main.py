from dotenv import find_dotenv, load_dotenv

from api.api import app

load_dotenv(find_dotenv())

app()
