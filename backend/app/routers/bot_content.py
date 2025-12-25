from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.bot_content import BotContentCreate, BotContentRead
from app.models.bot_content import BotContent
from app.core.database import get_db

router = APIRouter(prefix="/bot-content", tags=["bot-content"])


@router.post("/", response_model=BotContentRead)
async def create_content(content: BotContentCreate, db: AsyncSession = Depends(get_db)):
    new_content = BotContent(
        key=content.key,
        value=content.value
    )
    db.add(new_content)
    await db.commit()
    await db.refresh(new_content)
    return new_content


@router.get("/", response_model=List[BotContentRead])
async def list_content(db: AsyncSession = Depends(get_db)):
    result = await db.execute(BotContent.__table__.select())
    contents = result.scalars().all()
    return contents
