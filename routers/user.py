from fastapi import APIRouter, Depends
from pytest import Session

from db.database import get_db
from services.user_db import create_user
from schemas.user.user_schema import UserBaseSchema, UserDisplay


router = APIRouter(prefix="/user", tags=["user"])


@router.post("/signup", response_model=UserDisplay)
def signup(request: UserBaseSchema, db: Session = Depends(get_db)):
    return create_user(db, request)
