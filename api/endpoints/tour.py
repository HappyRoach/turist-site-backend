from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Header

from .. import crud
from .. import security
from ..schemas.tour import *
from ..utils.database import get_db, Session
from database.schemas.user import User

router = APIRouter()

@router.post("/", response_model=Tour)
def create_tour(
    tour: TourCreate, 
    db: Session = Depends(get_db),
    token: str = Query(..., description="JWT токен"),
):
    """Создать новый тур (только для администраторов)"""
    
    user_payload = security.verify_token(token)
    user = db.query(User).filter(User.id == user_payload.get("user_id")).first()
    
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    
    if user.role.name not in ["superadmin", "admin"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    return crud.create_tour(
        db=db,
        name=tour.name,
        description=tour.description,
        country=tour.country,
        city=tour.city,
        duration=tour.duration,
        operator=tour.operator,
        price=tour.price,
        image_url=tour.image_url,
        external_url=tour.external_url
    )

@router.get("/", response_model=List[Tour])
def get_tours(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    operator: Optional[str] = Query(None, description="Фильтр по туроператору"),
    db: Session = Depends(get_db)
):
    """Получить список всех туров с возможностью фильтрации по туроператору"""
    return crud.get_tours(db, skip=skip, limit=limit, operator=operator)

@router.get("/{tour_id}", response_model=Tour)
def get_tour(tour_id: int, db: Session = Depends(get_db)):
    """Получить информацию о конкретном туре"""
    db_tour = crud.get_tour(db, tour_id=tour_id)
    if db_tour is None:
        raise HTTPException(status_code=404, detail="Tour not found")
    return db_tour

@router.put("/{tour_id}", response_model=Tour)
def update_tour(
    tour_id: int, 
    tour: TourUpdate, 
    db: Session = Depends(get_db),
    token: str = Query(..., description="JWT токен"),
):
    """Обновить информацию о туре (только для администраторов)"""
    
    user_payload = security.verify_token(token)
    user = db.query(User).filter(User.id == user_payload.get("user_id")).first()
    
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    
    if user.role.name not in ["superadmin", "admin"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    update_data = tour.dict(exclude_unset=True)
    db_tour = crud.update_tour(db=db, tour_id=tour_id, **update_data)
    if db_tour is None:
        raise HTTPException(status_code=404, detail="Tour not found")
    return db_tour

@router.delete("/{tour_id}")
def delete_tour(
    tour_id: int, 
    db: Session = Depends(get_db),
    token: str = Query(..., description="JWT токен"),
):
    """Удалить тур (только для администраторов)"""
    
    user_payload = security.verify_token(token)
    user = db.query(User).filter(User.id == user_payload.get("user_id")).first()
    
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    
    if user.role.name not in ["superadmin", "admin"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    db_tour = crud.delete_tour(db, tour_id=tour_id)
    if db_tour is None:
        raise HTTPException(status_code=404, detail="Tour not found")
    return {"message": "Tour deleted successfully"}
