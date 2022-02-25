from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.post.post_schema import PostDisplay, PostCreate
from services.post import post_db


router = APIRouter(prefix="/post", tags=["post"])


valid_image_url_types = ["absolute", "relative"]


@router.post("/create", response_model=PostDisplay)
def create_post(request: PostCreate, db: Session = Depends(get_db)):
    if not request.image_url_type in valid_image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Parameter image_url_type can only take values 'absolute' or 'relative'",
        )
    return post_db.create_post(db, request)
