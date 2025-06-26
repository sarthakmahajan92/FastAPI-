from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username= Column(String(500), unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)

