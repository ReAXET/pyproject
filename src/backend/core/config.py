"""Project configuration settings."""
import os
import re
from typing import List, Tuple, Union, Optional
from backend.utils.logger import logger
from backend.models.base import BaseModel
from sqlalchemy import URL
from dotenv import load_dotenv

from functools import lru_cache


# Load the .env file
load_dotenv()

# Logger
logger = logger

# Create a wrap function using logger
def log_wrap(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Exception: {e}")
            return None
    return wrapper


# Database settings
class Settings(BaseModel):
    """Settings for the database."""
    DATABASE_URL: Union[URL, str] = os.getenv("DATABASE_URL", "")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "")
    DATABASE_USER: str = os.getenv("DATABASE_USER", "")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD", "")
    DATABASE_HOST: str = os.getenv("DATABASE_HOST", "")
    DATABASE_PORT: str = os.getenv("DATABASE_PORT", "")
    DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL", "")
    DATABASE_URI: Optional[str] = os.getenv("DATABASE_URI", "")



# Get the settings
@lru_cache
def get_settings() -> Settings:
    """Get the settings for the database."""
    return Settings()

settings = get_settings()




