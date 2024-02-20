"""Base model for all models to inherit from."""
from sqlalchemy import Column, Integer, DateTime, func, MetaData, Table
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.sql import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import declared_attr
from sqlalchemy.engine import Engine
from typing import List, Tuple
import os
import re

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
def backref_player_team_association():
    return relationship("Team", secondary=player_team_association, backref="players")

# Backref for team and player association
def backref_team_player_association():
    return relationship("Player", secondary=player_team_association, backref="teams")

# Create a wrap function using logger
def log_wrap(func):
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
    def create(self, session, **kwargs) -> 'BaseModel':
        """Create a new record in the database."""
        for key, value in kwargs.items():
            setattr(self, key, value)
        session.add(self)
        session.commit()
        return self

    @log_wrap
    def update(self, session, **kwargs) -> 'BaseModel':
        """Update a record in the database."""
        for key, value in kwargs.items():
            setattr(self, key, value)
        session.commit()
        return self

    @log_wrap
    def delete(self, session) -> 'BaseModel':
        """Delete a record in the database."""
        session.delete(self)
        session.commit()
        return self

    @log_wrap
    def get(self, session, id: int) -> 'BaseModel':
        """Get a record from the database."""
        return session.query(self.__class__).filter_by(id=id).first()

    @log_wrap
    def get_all(self, session) -> List['BaseModel']:
        """Get all records from the database."""
        return session.query(self.__class__).all()

    @log_wrap
    def get_all_with_limit(self, session, limit: int) -> List['BaseModel']:
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
    
    #@log_wrap
    #@staticmethod
    #def execute_query(query: str) -> List[Tuple]:
    #    """Execute a raw SQL query."""
    #    with engine.connect() as conn:
    #        result = conn.execute(query)
    #        return result.fetchall()
    
    @log_wrap
    @declared_attr.directive
    def __tablename__(cls):
        """Get the table name from the class name."""
        return re.sub(r'([a-z\d])([A-Z])', r'\1_\2', cls.__name__).lower()
    



