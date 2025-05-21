from typing import List, Tuple

from fastapi import APIRouter, Depends, HTTPException

from .. import crud
from .. import security
from ..schemas.destination import *
from ..utils.database import get_db, Session
from database.schemas.user import User

router = APIRouter()

@router.post("/", response_model=Tuple[Destination, DestinationResult])
def create_destination(destination: DestinationCreate, db: Session = Depends(get_db),
                      current_user: User = Depends(security.get_current_user_with_role)):
    db_destination, result = crud.create_destination(
        db=db,
        activity=destination.activity,
        climate=destination.climate,
        length=destination.length,
        transport=destination.transport,
        budget=destination.budget,
        user_id=current_user.id
    )
    return db_destination, {"destinations": result}

@router.get("/", response_model=List[Destination])
def get_destinations(db: Session = Depends(get_db),
                    current_user: User = Depends(security.check_role(["superadmin", "admin"]))):
    return crud.get_destinations(db)

@router.get("/me", response_model=List[Destination])
def get_user_destinations(db: Session = Depends(get_db),
                         current_user: User = Depends(security.get_current_user_with_role)):
    return crud.get_user_destinations(db, user_id=current_user.id)

@router.get("/{destination_id}", response_model=Destination)
def get_destination(destination_id: int, db: Session = Depends(get_db),
                   current_user: User = Depends(security.get_current_user_with_role)):
    db_destination = crud.get_destination(db, destination_id=destination_id)
    if db_destination is None:
        raise HTTPException(status_code=404, detail="Destination not found")
    if db_destination.user_id != current_user.id and current_user.role.name not in ["superadmin", "admin"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return db_destination

@router.delete("/{destination_id}")
def delete_destination(destination_id: int, db: Session = Depends(get_db),
                      current_user: User = Depends(security.get_current_user_with_role)):
    db_destination = crud.get_destination(db, destination_id=destination_id)
    if db_destination is None:
        raise HTTPException(status_code=404, detail="Destination not found")
    if db_destination.user_id != current_user.id and current_user.role.name not in ["superadmin", "admin"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    crud.delete_destination(db, destination_id=destination_id)
    return {"message": "Destination deleted successfully"} 