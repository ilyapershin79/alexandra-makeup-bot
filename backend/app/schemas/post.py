from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str
    media_url: Optional[str] = None


class PostCreate(PostBase):
    pass


class PostRead(PostBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
