"""Functions for creating and interacting with the postgres database."""
import os
from sqlalchemy import create_engine, text, MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from loguru import logger
from backend.core.config import settings


# Logger 
logger = logger

# Metadata
metadata = MetaData()


# Database engine
def create_engine_and_session():
    """Create a new engine and session."""
    SQL_URL = f"postgresql://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"
    engine = create_engine(SQL_URL)
    session = sessionmaker(engine)
    return engine, session


SQL_URL = f"postgresql://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"


ASYNC_SQL_URL = SQL_URL.replace("postgresql", "postgresql+asyncpg")

# Async database engine
async def create_async_engine_and_session():
    """Create a new async engine and session."""
    engine = create_async_engine(ASYNC_SQL_URL)
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
    return engine, async_session


# Create function that creates all tables that have inherited from BaseModel
def create_tables(engine):
    """Create all tables."""
    metadata.create_all(engine)


# Drop certain tables based on the table names
def drop_tables(engine, table_names) -> None:
    """Drop certain tables."""
    metadata.drop_all(engine, tables=table_names)


# Test the connection to the database
db_url = os.getenv("DATABASE_URI")


def get_db():
    """Return the database connection."""
    db = create_engine_and_session(db_url)
    try:
        yield db
        logger.info("Database connection successful.")
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise e
    
    finally:
        db.close()
        logger.info("Database connection closed.")

# Test the connection to the database
def test_connection():
    """Test the connection to the database."""
    try:
        engine = create_engine(db_url)
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            logger.info("Database connection successful.")
            return result
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise e
    finally:
        conn.close()
        logger.info("Database connection closed.")

# Test the connection to the database
test_connection()




   