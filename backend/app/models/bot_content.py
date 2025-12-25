from sqlalchemy import Column, Integer, String
from app.core.database import Base


class BotContent(Base):
    __tablename__ = "bot_content"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, nullable=False)  # Например: 'welcome_text', 'about_text'
    value = Column(String, nullable=False)
