from fastapi import FastAPI
from .db import db_init, DB_PATH
from .routers import posts

app = FastAPI()

db_init()

app.include_router(posts.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
