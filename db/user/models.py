from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer

from db.database import base as Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(256), nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    posts = relationship("Post", back_populates="user")
