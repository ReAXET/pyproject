"""Base model for all models to inherit from."""
from sqlalchemy import Column, Integer, DateTime, func, MetaData, Table
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.engine import Engine
from typing import List, Tuple
import os
from backend.database.db import engine
