from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(UserBaseSchema):
    username: str
    email: str

    class Config:
        orm_mode = True
