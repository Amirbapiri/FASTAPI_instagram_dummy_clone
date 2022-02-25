from datetime import datetime

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
