from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.core.database import Base


class Giveaway(Base):
    __tablename__ = "giveaways"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    prize = Column(String, nullable=False)
    codeword = Column(String, nullable=False)
    instagram_link = Column(String, nullable=True)
    ended = Column(Boolean, default=False)
    winner_name = Column(String, nullable=True)
    end_date = Column(DateTime, nullable=True)
