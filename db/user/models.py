from db.database import base as Base

from sqlalchemy import Column, String, Integer, null


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(256), nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
