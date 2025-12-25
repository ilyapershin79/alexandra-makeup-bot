from pydantic import BaseModel


class GiveawayParticipantBase(BaseModel):
    giveaway_id: int
    user_id: int


class GiveawayParticipantCreate(GiveawayParticipantBase):
    pass


class GiveawayParticipantRead(GiveawayParticipantBase):
    id: int

    class Config:
        orm_mode = True
