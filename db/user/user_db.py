from schemas.user import user_schema
from sqlalchemy.orm import Session

from db.user.models import User


def create_user(db: Session, request: user_schema.UserBaseSchema):
    user = User(
        username=request.username,
        email=request.email,
        # TODO save hashed version of password
        password=request.password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
