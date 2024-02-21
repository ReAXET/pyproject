"""Base Paths for the project"""
import os

from loguru import logger

log = logger.bind(name=__file__)


# Base path for the project
BASE_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__)))))

# Path to the Source directory
SRC_PATH = os.path.join(BASE_PATH, 'src')

# Path to the Backend directory
BACKEND_PATH = os.path.join(SRC_PATH, 'backend')

# Path to the Core directory
CORE_PATH = os.path.join(BACKEND_PATH, 'core')

# Path to the Data directory
DATA_PATH = os.path.join(BACKEND_PATH, 'data')
log.debug(f"DATA_PATH: {DATA_PATH}")

# Path to the NBA Data directory
NBA_DATA_PATH = os.path.join(DATA_PATH, 'nba')


PKG_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
log.debug(f"PKG_ROOT: {PKG_ROOT}")
