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
