from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    phone_no = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)