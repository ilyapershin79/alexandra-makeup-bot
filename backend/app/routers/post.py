from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.post import PostCreate, PostRead
from app.models.post import Post
from app.core.database import get_db

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/", response_model=PostRead)
async def create_post(post: PostCreate, db: AsyncSession = Depends(get_db)):
    new_post = Post(
        title=post.title,
        content=post.content,
        media_url=post.media_url
    )
    db.add(new_post)
    await db.commit()
    await db.refresh(new_post)
    return new_post


@router.get("/", response_model=List[PostRead])
async def list_posts(db: AsyncSession = Depends(get_db)):
    result = await db.execute(Post.__table__.select())
    posts = result.scalars().all()
    return posts
