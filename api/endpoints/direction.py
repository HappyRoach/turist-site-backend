from typing import List
from fastapi import APIRouter, Depends, HTTPException
from .. import crud, security
from ..schemas.direction import Direction, DirectionCreate, DirectionUpdate
from ..utils.database import get_db, Session
from database.schemas.user import User

router = APIRouter()

@router.get("/", response_model=List[Direction])
def list_directions(db: Session = Depends(get_db)):
    return crud.get_directions(db)

@router.post("/", response_model=Direction)
def create_direction(
    direction: DirectionCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(security.check_role(["superadmin", "admin"]))
):
    try:
        return crud.create_direction(db, name=direction.name)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Direction with this name already exists")

@router.put("/{direction_id}", response_model=Direction)
def update_direction(
    direction_id: int,
    direction: DirectionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(security.check_role(["superadmin", "admin"]))
):
    db_dir = crud.update_direction(db, direction_id=direction_id, name=direction.name)
    if not db_dir:
        raise HTTPException(status_code=404, detail="Direction not found")
    return db_dir

@router.delete("/{direction_id}")
def delete_direction(
    direction_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(security.check_role(["superadmin", "admin"]))
):
    db_dir = crud.delete_direction(db, direction_id=direction_id)
    if not db_dir:
        raise HTTPException(status_code=404, detail="Direction not found")
    return {"message": "Direction deleted successfully"}
