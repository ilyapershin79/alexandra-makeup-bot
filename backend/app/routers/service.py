from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.service import ServiceCreate, ServiceRead
from app.models.service import Service
from app.core.database import get_db

router = APIRouter(prefix="/services", tags=["services"])


@router.post("/", response_model=ServiceRead)
async def create_service(service: ServiceCreate, db: AsyncSession = Depends(get_db)):
    new_service = Service(
        title=service.title,
        description=service.description,
        price=service.price
    )
    db.add(new_service)
    await db.commit()
    await db.refresh(new_service)
    return new_service


@router.get("/", response_model=List[ServiceRead])
async def list_services(db: AsyncSession = Depends(get_db)):
    result = await db.execute(Service.__table__.select())
    services = result.scalars().all()
    return services
