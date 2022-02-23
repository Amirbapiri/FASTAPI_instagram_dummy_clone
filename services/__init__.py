from fastapi import Depends

from sqlalchemy.orm import Session
from db.database import get_db

def create_user(db: Session = Depends(get_db), request: UserSchema):
    pass