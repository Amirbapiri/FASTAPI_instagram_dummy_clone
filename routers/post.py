import shutil
from typing import List
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.post.post_schema import PostDisplay, PostCreate
from schemas.user.user_schema import UserAuth
from services.post import post_db
from utils.filename_generator import generate_random_string
from auth.oauth2 import get_current_user


router = APIRouter(prefix="/post", tags=["post"])


valid_image_url_types = ["absolute", "relative"]


@router.post("/create", response_model=PostDisplay)
def create_post(
    request: PostCreate,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user),
):
    if not request.image_url_type in valid_image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Parameter image_url_type can only take values 'absolute' or 'relative'",
        )
    return post_db.create_post(db, request)


@router.get("/all", response_model=List[PostDisplay])
def get_posts(db: Session = Depends(get_db)):
    return post_db.get_posts(db)


@router.post("/image/upload")
def upload_image(
    image: UploadFile = File(...),
    current_user: UserAuth = Depends(get_current_user),
):
    filename = generate_random_string(image.filename)
    upload_to = f"images/{filename}"

    with open(upload_to, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)
    return {"filename": upload_to}


@router.delete("/delete/{id}")
def delete_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user),
):
    return post_db.delete(db, id, current_user.id)
