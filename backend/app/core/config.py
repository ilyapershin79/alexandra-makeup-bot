from pydantic import BaseModel
import os


class Settings(BaseModel):
    BOT_TOKEN: str
    BACKEND_URL: str
    DATABASE_URL: str


settings = Settings(
    BOT_TOKEN=os.getenv("BOT_TOKEN", ""),
    BACKEND_URL=os.getenv("BACKEND_URL", ""),
    DATABASE_URL=os.getenv("DATABASE_URL", ""),
)
