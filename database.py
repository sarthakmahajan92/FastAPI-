from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:1234@localhost:5432/postgres"

engine = create_engine("postgresql://postgres:1234@localhost:5432/postgres")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


#Base variable is used to create table in main.py.
#declarative base() is a function that constract a base class for declarative class.
#engine is the actual database connection.




