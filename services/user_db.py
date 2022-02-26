from fastapi import HTTPException, status
from schemas.user import user_schema
from sqlalchemy.orm import Session

from db.user.models import User
from utils.hasher import Hash


def create_user(db: Session, request: user_schema.UserBaseSchema):
    user = User(
        username=request.username,
        email=request.email,
        password=Hash.hash(request.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_username(db: Session, username: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with username {username} doesn't exist",
        )
    return user
