from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .. import Base

class SurveyQuestion(Base):
    __tablename__ = 'survey_questions'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)

    answers = relationship("SurveyAnswer", back_populates="question", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<SurveyQuestion(title='{self.title[:30]}', id='{self.id}')>"

class SurveyAnswer(Base):
    __tablename__ = 'survey_answers'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(500), nullable=False)
    criterion = Column(String(100), nullable=False)  # e.g., 'Развлекательность', etc.
    score = Column(Integer, nullable=False, default=0)
    question_id = Column(Integer, ForeignKey('survey_questions.id', ondelete='CASCADE'), nullable=False)

    question = relationship("SurveyQuestion", back_populates="answers")

    def __repr__(self):
        return f"<SurveyAnswer(text='{self.text[:30]}', score={self.score}, id='{self.id}')>"
