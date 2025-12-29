import os

from dotenv import load_dotenv

load_dotenv()

class _Settings:
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

Settings = _Settings()