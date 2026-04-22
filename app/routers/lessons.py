from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.models.lesson import LessonDB
from app.schemas.lesson import LessonRead

router = APIRouter(prefix="/lessons", tags=["lessons"])


@router.get("/", response_model=list[LessonRead])
def get_lessons(db: Session = Depends(get_db)):
    lessons = db.scalars(select(LessonDB)).all()
    return lessons
