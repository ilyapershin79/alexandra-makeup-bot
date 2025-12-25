from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.giveaway import GiveawayCreate, GiveawayRead
from app.models.giveaway import Giveaway
from app.core.database import get_db

router = APIRouter(prefix="/giveaways", tags=["giveaways"])


@router.post("/", response_model=GiveawayRead)
async def create_giveaway(giveaway: GiveawayCreate, db: AsyncSession = Depends(get_db)):
    new_giveaway = Giveaway(
        title=giveaway.title,
        prize=giveaway.prize,
        codeword=giveaway.codeword,
        instagram_link=giveaway.instagram_link,
        ended=giveaway.ended,
        winner_name=giveaway.winner_name,
        end_date=giveaway.end_date
    )
    db.add(new_giveaway)
    await db.commit()
    await db.refresh(new_giveaway)
    return new_giveaway


@router.get("/", response_model=List[GiveawayRead])
async def list_giveaways(db: AsyncSession = Depends(get_db)):
    result = await db.execute(Giveaway.__table__.select())
    giveaways = result.scalars().all()
    return giveaways
