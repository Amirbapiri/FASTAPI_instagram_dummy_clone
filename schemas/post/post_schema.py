from datetime import datetime
from pydantic import BaseModel


class PostBaseSchema(BaseModel):
    title: str
    description: str
    image_url: str
    image_url_type: str


class PostCreate(PostBaseSchema):
    title: str
    description: str
    creator_id: int


class User(BaseModel):
    # Schema of User to display posts
    username: str

    class Config:
        orm_mode = True


class PostDisplay(PostBaseSchema):
    id: int
    user: User
    created_at: datetime

    class Config:
        orm_mode = True
