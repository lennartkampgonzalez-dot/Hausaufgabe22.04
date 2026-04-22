from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import FRONTEND_ORIGIN
from app.core.db import Base, SessionLocal, engine
from app.models import AnswerOptionDB, LessonDB, QuizQuestionDB  # noqa: F401 – registers models with Base
from app.routers import lessons, quiz
from app.services.seed_service import seed_lessons, seed_quiz_questions

app = FastAPI(title="ReactQuest API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(lessons.router)
app.include_router(quiz.router)


@app.on_event("startup")
def on_startup() -> None:
    # Create tables if they don't exist yet
    Base.metadata.create_all(bind=engine)

    # Import JSON seed data once
    db = SessionLocal()
    try:
        seed_lessons(db)
        seed_quiz_questions(db)
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "ReactQuest API is running."}
