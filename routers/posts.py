from fastapi import APIRouter
from typing import List, Union
from pydantic import BaseModel
import sqlite3
from ..db import DB_PATH

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
)

class Post(BaseModel):
    slug: str
    title: Union[str, None]
    introduction: Union[str, None]
    content: Union[str, None]
    year: Union[int, None]
    publish_date: Union[str, None]

@router.get("/")
def get_posts() -> List[Post]:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT slug, title, introduction, content, year, publish_date FROM posts"
    )
    return_list = []
    for slug, title, introduction, content, year, publish_date in cursor:
        return_list.append(
            Post(
                slug=slug,
                title=title,
                introduction=introduction,
                content=content,
                year=year,
                publish_date=publish_date,
            )
        )
    connection.close()
    return return_list
