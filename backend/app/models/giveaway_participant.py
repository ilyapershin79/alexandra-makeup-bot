from sqlalchemy import Column, Integer, ForeignKey
from app.core.database import Base


class GiveawayParticipant(Base):
    __tablename__ = "giveaway_participants"

    id = Column(Integer, primary_key=True, index=True)
    giveaway_id = Column(Integer, ForeignKey("giveaways.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
