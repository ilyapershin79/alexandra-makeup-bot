from sqlalchemy import Column, Integer, ForeignKey
from app.core.database import Base


class CourseAccess(Base):
    __tablename__ = "course_access"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
