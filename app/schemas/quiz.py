from pydantic import BaseModel


class AnswerOptionRead(BaseModel):
    id: str
    text: str
    is_correct: bool

    model_config = {"from_attributes": True}


class QuizQuestionRead(BaseModel):
    id: str
    question: str
    explanation: str
    answers: list[AnswerOptionRead]

    model_config = {"from_attributes": True}
