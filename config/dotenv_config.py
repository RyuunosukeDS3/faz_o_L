from dotenv import load_dotenv
from os import getenv

class Config:
    load_dotenv()
    api_key = getenv("API_KEY")
    api_key_secret = getenv("API_KEY_SECRET")
    access_token = getenv("ACCESS_TOKEN")
    access_token_secret = getenv("ACCESS_TOKEN_SECRET")
    bearer_token = getenv("BEARER_TOKEN")
    author_id = getenv("AUTHOR_ID")
