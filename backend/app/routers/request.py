from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.request import RequestCreate, RequestRead
from app.models.request import Request
from app.core.database import get_db

router = APIRouter(prefix="/requests", tags=["requests"])


@router.post("/", response_model=RequestRead)
async def create_request(request: RequestCreate, db: AsyncSession = Depends(get_db)):
    new_request = Request(
        user_id=request.user_id,
        type=request.type,
        item_title=request.item_title,
        contact=request.contact,
        comment=request.comment
    )
    db.add(new_request)
    await db.commit()
    await db.refresh(new_request)
    return new_request


@router.get("/", response_model=List[RequestRead])
async def list_requests(db: AsyncSession = Depends(get_db)):
    result = await db.execute(Request.__table__.select())
    requests = result.scalars().all()
    return requests
