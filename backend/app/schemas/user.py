from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    telegram_id: str
    name: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int
    registered_at: datetime
    last_active: datetime

    class Config:
        orm_mode = True
