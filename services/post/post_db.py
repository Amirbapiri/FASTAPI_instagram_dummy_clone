from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from db.post.models import Post
from schemas.post.post_schema import PostCreate


def create_post(db: Session, request: PostCreate):
    post = Post(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        title=request.title,
        description=request.description,
        created_at=datetime.now(),
        user_id=request.creator_id,
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def get_posts(db: Session):
    """
    This method returns all posts back
    """
    return db.query(Post).all()


def delete(db: Session, id: int, user_id: int):
    post = db.query(Post).filter(Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Couldn't find any post with id {id}",
        )
    if post.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
        )
    db.delete(post)
    db.commit()
    return True
