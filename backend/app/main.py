import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import (
    user,
    course,
    service,
    request,
    giveaway,
    giveaway_participant,
    post,
    course_access,
    bot_content,
)

app = FastAPI(title="Alexandra Makeup Bot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(course.router)
app.include_router(service.router)
app.include_router(request.router)
app.include_router(giveaway.router)
app.include_router(giveaway_participant.router)
app.include_router(post.router)
app.include_router(course_access.router)
app.include_router(bot_content.router)

# 👇 ВАЖНО ДЛЯ RAILWAY
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)
