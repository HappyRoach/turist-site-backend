from typing import List
from fastapi import APIRouter, Depends, HTTPException
from .. import crud, security
from ..schemas.survey import SurveyQuestion, SurveyQuestionCreate, SurveyQuestionUpdate, SurveyAnswer, SurveyAnswerCreate
from ..utils.database import get_db, Session
from database.schemas.user import User

router = APIRouter()

@router.get("/", response_model=List[SurveyQuestion])
def list_questions(db: Session = Depends(get_db)):
    return crud.get_questions(db)

@router.post("/", response_model=SurveyQuestion)
def create_question(
    question: SurveyQuestionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(security.check_role(["superadmin", "admin"]))
):
    db_question = crud.create_question(db, title=question.title)
    for ans in question.answers:
        crud.add_answer(db, question_id=db_question.id, text=ans.text, criterion=ans.criterion, score=ans.score)
    db.refresh(db_question)
    return db_question

@router.put("/{question_id}", response_model=SurveyQuestion)
def update_question(
    question_id: int,
    question: SurveyQuestionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(security.check_role(["superadmin", "admin"]))
):
    db_question = crud.get_question(db, question_id)
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    if question.title is not None:
        crud.update_question(db, question_id, title=question.title)
    db.refresh(db_question)
    return db_question

@router.delete("/{question_id}")
def delete_question(
    question_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(security.check_role(["superadmin", "admin"]))
):
    db_question = crud.delete_question(db, question_id=question_id)
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    return {"message": "Question deleted successfully"}

# Answer endpoints
@router.post("/{question_id}/answers", response_model=SurveyAnswer)
def create_answer(
    question_id: int,
    answer: SurveyAnswerCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(security.check_role(["superadmin", "admin"]))
):
    db_question = crud.get_question(db, question_id)
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    return crud.add_answer(db, question_id=question_id, text=answer.text, criterion=answer.criterion, score=answer.score)

@router.put("/answers/{answer_id}", response_model=SurveyAnswer)
def update_answer(
    answer_id: int,
    answer: SurveyAnswerCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(security.check_role(["superadmin", "admin"]))
):
    db_ans = crud.update_answer(db, answer_id=answer_id, text=answer.text, criterion=answer.criterion, score=answer.score)
    if not db_ans:
        raise HTTPException(status_code=404, detail="Answer not found")
    return db_ans

@router.delete("/answers/{answer_id}")
def delete_answer(
    answer_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(security.check_role(["superadmin", "admin"]))
):
    db_ans = crud.delete_answer(db, answer_id=answer_id)
    if not db_ans:
        raise HTTPException(status_code=404, detail="Answer not found")
    return {"message": "Answer deleted successfully"}
