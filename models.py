from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    registration_number = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)  # Hashed password
    course = Column(String, nullable=False)  # BCA, BTech, MBA, Fashion, BioTech
    phone = Column(String, nullable=False)
    residence = Column(String, nullable=False)
