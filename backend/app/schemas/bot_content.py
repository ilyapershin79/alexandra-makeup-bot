from pydantic import BaseModel


class BotContentBase(BaseModel):
    key: str
    value: str


class BotContentCreate(BotContentBase):
    pass


class BotContentRead(BotContentBase):
    id: int

    class Config:
        orm_mode = True
