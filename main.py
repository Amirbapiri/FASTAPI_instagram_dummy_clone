from fastapi import FastAPI

from db.user import models as user_model
from db.database import engine

app = FastAPI()


@app.get("/")
def index():
    return "Hello dear user :)"


user_model.Base.metadata.create_all(bind=engine)