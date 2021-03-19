from fastapi import FastAPI

from blog.routers import user as user_router
from blog.routers import blog as blog_router
from blog.routers import authentication as authentication_router

from blog import models
from blog.database import engine

# create or update the db
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(authentication_router.router)
app.include_router(blog_router.router)
app.include_router(user_router.router)
