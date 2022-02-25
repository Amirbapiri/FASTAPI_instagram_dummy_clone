from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from db.user import models as user_model
from db.database import engine

# registering routers
from routers.user import router as user_router
from routers.post import router as post_router
from auth.authentication import router as auth_router

app = FastAPI()


app.include_router(user_router)
app.include_router(auth_router)
app.include_router(post_router)


@app.get("/")
def index():
    return "Hello dear user :)"


user_model.Base.metadata.create_all(bind=engine)

app.mount("/images", StaticFiles(directory="images"), name="images")
