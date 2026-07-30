import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

    BLOB_CONNECTION_STRING = os.getenv("BLOB_CONNECTION_STRING")
    BLOB_CONTAINER = os.getenv("BLOB_CONTAINER")