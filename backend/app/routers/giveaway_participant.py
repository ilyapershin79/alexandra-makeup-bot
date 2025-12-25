from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.giveaway_participant import GiveawayParticipantCreate, GiveawayParticipantRead
from app.models.giveaway_participant import GiveawayParticipant
from app.core.database import get_db

router = APIRouter(prefix="/giveaway-participants", tags=["giveaway-participants"])


@router.post("/", response_model=GiveawayParticipantRead)
async def create_participant(participant: GiveawayParticipantCreate, db: AsyncSession = Depends(get_db)):
    new_participant = GiveawayParticipant(
        giveaway_id=participant.giveaway_id,
        user_id=participant.user_id
    )
    db.add(new_participant)
    await db.commit()
    await db.refresh(new_participant)
    return new_participant


@router.get("/", response_model=List[GiveawayParticipantRead])
async def list_participants(db: AsyncSession = Depends(get_db)):
    result = await db.execute(GiveawayParticipant.__table__.select())
    participants = result.scalars().all()
    return participants
