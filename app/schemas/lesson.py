from pydantic import BaseModel


class LessonRead(BaseModel):
    id: str
    title: str
    topic: str
    type: str
    level: str
    content: str

    model_config = {"from_attributes": True}
