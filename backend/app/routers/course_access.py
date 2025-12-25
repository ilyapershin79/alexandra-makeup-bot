from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.course_access import CourseAccessCreate, CourseAccessRead
from app.models.course_access import CourseAccess
from app.core.database import get_db

router = APIRouter(prefix="/course-access", tags=["course-access"])


@router.post("/", response_model=CourseAccessRead)
async def create_course_access(access: CourseAccessCreate, db: AsyncSession = Depends(get_db)):
    new_access = CourseAccess(
        user_id=access.user_id,
        course_id=access.course_id
    )
    db.add(new_access)
    await db.commit()
    await db.refresh(new_access)
    return new_access


@router.get("/", response_model=List[CourseAccessRead])
async def list_course_access(db: AsyncSession = Depends(get_db)):
    result = await db.execute(CourseAccess.__table__.select())
    accesses = result.scalars().all()
    return accesses
