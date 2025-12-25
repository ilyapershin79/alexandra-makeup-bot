from pydantic import BaseModel
from typing import Optional


class CourseBase(BaseModel):
    title: str
    short_description: str
    full_description: str
    price: float
    old_price: Optional[float] = None
    is_promo: Optional[bool] = False
    youtube_link: Optional[str] = None
    drive_link: Optional[str] = None
    telegram_channel: Optional[str] = None


class CourseCreate(CourseBase):
    pass


class CourseRead(CourseBase):
    id: int

    class Config:
        orm_mode = True
