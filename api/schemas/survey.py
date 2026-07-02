from pydantic import BaseModel, Field
from typing import List, Optional

class SurveyAnswerBase(BaseModel):
    text: str = Field(..., description="Текст ответа")
    criterion: str = Field(..., description="Критерий оценки")
    score: int = Field(..., description="Балл от -10 до 10")

class SurveyAnswerCreate(SurveyAnswerBase):
    pass

class SurveyAnswer(SurveyAnswerBase):
    id: int
    question_id: int

    class Config:
        from_attributes = True

class SurveyQuestionBase(BaseModel):
    title: str = Field(..., description="Текст вопроса")

class SurveyQuestionCreate(SurveyQuestionBase):
    answers: List[SurveyAnswerCreate] = []

class SurveyQuestionUpdate(BaseModel):
    title: Optional[str] = None

class SurveyQuestion(SurveyQuestionBase):
    id: int
    answers: List[SurveyAnswer] = []

    class Config:
        from_attributes = True
