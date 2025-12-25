from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.course import CourseCreate, CourseRead
from app.models.course import Course
from app.core.database import get_db

router = APIRouter(prefix="/courses", tags=["courses"])


@router.post("/", response_model=CourseRead)
async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_db)):
    new_course = Course(
        title=course.title,
        short_description=course.short_description,
        full_description=course.full_description,
        price=course.price,
        old_price=course.old_price,
        is_promo=course.is_promo,
        youtube_link=course.youtube_link,
        drive_link=course.drive_link,
        telegram_channel=course.telegram_channel
    )
    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)
    return new_course


@router.get("/", response_model=List[CourseRead])
async def list_courses(db: AsyncSession = Depends(get_db)):
    result = await db.execute(Course.__table__.select())
    courses = result.scalars().all()
    return courses
