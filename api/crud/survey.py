from sqlalchemy.orm import Session
from database.schemas.survey import SurveyQuestion, SurveyAnswer
from typing import Optional, List, Dict, Any

def create_question(db: Session, title: str):
    db_question = SurveyQuestion(title=title)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def get_questions(db: Session):
    return db.query(SurveyQuestion).all()

def get_question(db: Session, question_id: int):
    return db.query(SurveyQuestion).filter(SurveyQuestion.id == question_id).first()

def update_question(db: Session, question_id: int, title: str):
    db_question = get_question(db, question_id)
    if db_question:
        db_question.title = title
        db.commit()
        db.refresh(db_question)
    return db_question

def delete_question(db: Session, question_id: int):
    db_question = get_question(db, question_id)
    if db_question:
        db.delete(db_question)
        db.commit()
    return db_question

# Answers CRUD
def add_answer(db: Session, question_id: int, text: str, criterion: str, score: int):
    db_answer = SurveyAnswer(
        question_id=question_id,
        text=text,
        criterion=criterion,
        score=score
    )
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer

def update_answer(db: Session, answer_id: int, text: Optional[str] = None, criterion: Optional[str] = None, score: Optional[int] = None):
    db_answer = db.query(SurveyAnswer).filter(SurveyAnswer.id == answer_id).first()
    if db_answer:
        if text is not None:
            db_answer.text = text
        if criterion is not None:
            db_answer.criterion = criterion
        if score is not None:
            db_answer.score = score
        db.commit()
        db.refresh(db_answer)
    return db_answer

def delete_answer(db: Session, answer_id: int):
    db_answer = db.query(SurveyAnswer).filter(SurveyAnswer.id == answer_id).first()
    if db_answer:
        db.delete(db_answer)
        db.commit()
    return db_answer
