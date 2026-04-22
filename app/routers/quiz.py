from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.core.deps import get_db
from app.models.quiz import QuizQuestionDB
from app.schemas.quiz import QuizQuestionRead

router = APIRouter(prefix="/quiz-questions", tags=["quiz"])


@router.get("/", response_model=list[QuizQuestionRead])
def get_quiz_questions(db: Session = Depends(get_db)):
    stmt = select(QuizQuestionDB).options(selectinload(QuizQuestionDB.answers))
    questions = db.scalars(stmt).all()
    return questions
