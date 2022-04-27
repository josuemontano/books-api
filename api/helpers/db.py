import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = os.getenv("DATABASE_URL")
if db_url is None:
    raise RuntimeError("DATABSE_URL environment variable is not set")

engine = create_engine(db_url)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """The Session, whenever it is used to talk to the database, begins a database
    transaction as soon as it starts communicating.

    The Session will begin a new transaction if it is used again, subsequent to
    the previous transaction ending, therefore the Session is capable of having
    a lifespan across many transactions, though only one at a time.
    """
    db = SessionFactory()

    try:
        yield db
    finally:
        db.close()


class DBContextManager:
    """Context manager for SQLAlchemy database sessions. Creates a session on
    enter and closes it on exit.

    :example:
    with DBContextManager() as db:
        pass
    """

    def __init__(self):
        self.db = SessionFactory()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()
