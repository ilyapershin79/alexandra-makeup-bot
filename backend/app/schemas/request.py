from pydantic import BaseModel
from typing import Optional


class RequestBase(BaseModel):
    type: str  # "course" или "service"
    item_title: str
    contact: str
    comment: Optional[str] = None


class RequestCreate(RequestBase):
    user_id: int


class RequestRead(RequestBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
