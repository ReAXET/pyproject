"""Base model for all models to inherit from."""
import os
import re
from typing import List, Tuple, Any, Callable, Self

from sqlalchemy import Column, DateTime, Integer, MetaData, Table, func
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Relationship
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, declared_attr, relationship
from sqlalchemy.sql import select

from backend.utils.logger import logger

metadata = MetaData()

# Player and team association table
player_team_association = Table(
    'player_team_association',
    metadata,
    Column('player_id', Integer, primary_key=True),
    Column('team_id', Integer, primary_key=True)
)

# Backref for player and team association


def backref_player_team_association() -> Relationship[Any]:
    return relationship("Team", secondary=player_team_association, backref="players")

# Backref for team and player association


def backref_team_player_association() -> Relationship[Any]:
    return relationship("Player", secondary=player_team_association, backref="teams")

# Create a wrap function using logger


def log_wrap(func) -> Callable[..., Any | None]:
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except SQLAlchemyError as e:
            logger.error(f"SQLAlchemyError: {e}")
            return None
        except Exception as e:
            logger.error(f"Exception: {e}")
            return None
    return wrapper


class BaseModel(DeclarativeBase):
    """Base model for all models to inherit from."""
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    @log_wrap
    def create(self, session, **kwargs) -> Self:
        """Create a new record in the database."""
        for key, value in kwargs.items():
            setattr(self, key, value)
        session.add(self)
        session.commit()
        return self

    @log_wrap
    def update(self, session, **kwargs) -> Self:
        """Update a record in the database."""
        for key, value in kwargs.items():
            setattr(self, key, value)
        session.commit()
        return self

    @log_wrap
    def delete(self, session) -> Self:
        """Delete a record in the database."""
        session.delete(self)
        session.commit()
        return self

    @log_wrap
    def get(self, session, id: int) -> Self:
        """Get a record from the database."""
        return session.query(self.__class__).filter_by(id=id).first()

    @log_wrap
    def get_all(self, session) -> List[Self]:
        """Get all records from the database."""
        return session.query(self.__class__).all()

    @log_wrap
    def get_all_with_limit(self, session, limit: int) -> List[Self]:
        """Get all records from the database with a limit."""
        return session.query(self.__class__).limit(limit).all()

    @log_wrap
    def get_all_with_offset(self, session, offset: int) -> List['BaseModel']:
        """Get all records from the database with an offset."""
        return session.query(self.__class__).offset(offset).all()

    @log_wrap
    def get_all_with_limit_and_offset(self, session, limit: int, offset: int) -> List['BaseModel']:
        """Get all records from the database with a limit and an offset."""
        return session.query(self.__class__).limit(limit).offset(offset).all()

    @log_wrap
    def get_all_with_filter(self, session, **kwargs) -> List['BaseModel']:
        """
        Retrieve all instances of the model with the specified filter.

        Args:
        - session: The database session
        - **kwargs: Key-value pairs to filter the instances

        Returns:
        - List['BaseModel']: List of instances matching the filter
        """
        return session.query(self.__class__).filter_by(**kwargs).all()

    @log_wrap
    def get_all_with_filter_and_limit(self, session, limit: int, **kwargs) -> List['BaseModel']:
        """
        Get all records from the database with a filter.

        Args:
            session: The database session.
            **kwargs: Filtering criteria.

        Returns:
            A list of BaseModel instances that meet the filter criteria.
        """
        return session.query(self.__class__).filter_by(**kwargs).limit(limit).all()

    # @log_wrap
    # @staticmethod
    # def execute_query(query: str) -> List[Tuple]:
    #    """Execute a raw SQL query."""
    #    with engine.connect() as conn:
    #        result = conn.execute(query)
    #        return result.fetchall()

    @log_wrap
    @declared_attr.directive
    def __tablename__(cls):
        """Get the table name from the class name."""
        return re.sub(r'([a-z\d])([A-Z])', r'\1_\2', cls.__name__).lower()
