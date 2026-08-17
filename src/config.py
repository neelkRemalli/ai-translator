import os
from dotenv import load_dotenv
from src.exceptions import ConfigurationError

load_dotenv()

class Settings:
    API_KEY = os.getenv("OPENROUTER_API_KEY")
    BASE_URL = os.getenv("OPENROUTER_BASE_URL")
    MODEL_NAME = "openai/gpt-oss-20b:free"
    REQUEST_TIMEOUT = 30
    MAX_RETRIES = 3
    


if not Settings.API_KEY:
    raise ConfigurationError("OPENROUTER_API_KEY is missing in .env")


        