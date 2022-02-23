from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./ig_db.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

local_session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

base = declarative_base()


def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()
