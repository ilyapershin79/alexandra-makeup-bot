from sqlalchemy import Column, Integer, String, Float, Boolean
from app.core.database import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    short_description = Column(String, nullable=False)
    full_description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    old_price = Column(Float, nullable=True)
    is_promo = Column(Boolean, default=False)
    youtube_link = Column(String, nullable=True)
    drive_link = Column(String, nullable=True)
    telegram_channel = Column(String, nullable=True)
