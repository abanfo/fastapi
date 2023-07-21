from fastapi import FastAPI
from routers.schemas import PostBase
from db import db_post
from routers import post,user
from db import model
from db.database import engine
from auth import authentication
from pydantic import BaseSettings
from routers import vote


app = FastAPI()
app.include_router(post.router)
app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(vote.router)


# @app.get('/posts')
# def get():
#     return db_post.get_all()

model.Base.metadata.create_all(bind=engine)
