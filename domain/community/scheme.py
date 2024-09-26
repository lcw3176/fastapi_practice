import datetime

from typing import List
from pydantic import BaseModel


class PostDto(BaseModel):
    id: int
    writer: str
    title: str
    comment_count: int
    create_date: datetime.datetime


class PostListResponse(BaseModel):
    total_page: int
    posts: List[PostDto]


class PostRegisterRequest(BaseModel):
    writer: str
    title: str
    content: str
    password: str

    