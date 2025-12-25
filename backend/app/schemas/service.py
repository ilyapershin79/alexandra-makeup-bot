from pydantic import BaseModel


class ServiceBase(BaseModel):
    title: str
    description: str
    price: float


class ServiceCreate(ServiceBase):
    pass


class ServiceRead(ServiceBase):
    id: int

    class Config:
        orm_mode = True
