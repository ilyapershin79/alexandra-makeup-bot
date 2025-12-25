from pydantic import BaseModel


class CourseAccessBase(BaseModel):
    user_id: int
    course_id: int


class CourseAccessCreate(CourseAccessBase):
    pass


class CourseAccessRead(CourseAccessBase):
    id: int

    class Config:
        orm_mode = True
