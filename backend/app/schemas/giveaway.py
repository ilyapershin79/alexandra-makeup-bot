from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class GiveawayBase(BaseModel):
    title: str
    prize: str
    codeword: str
    instagram_link: Optional[str] = None
    ended: Optional[bool] = False
    winner_name: Optional[str] = None
    end_date: Optional[datetime] = None


class GiveawayCreate(GiveawayBase):
    pass


class GiveawayRead(GiveawayBase):
    id: int

    class Config:
        orm_mode = True
