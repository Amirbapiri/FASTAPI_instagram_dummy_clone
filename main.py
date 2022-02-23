from fastapi import FastAPI

from db.user import models as user_model
from db.database import engine

# registering routers
from routers.user import router as user_router

app = FastAPI()


app.include_router(user_router)


@app.get("/")
def index():
    return "Hello dear user :)"


user_model.Base.metadata.create_all(bind=engine)
