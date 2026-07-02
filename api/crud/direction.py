from sqlalchemy.orm import Session
from database.schemas.direction import Direction
from typing import Optional, List

def create_direction(db: Session, name: str):
    db_direction = Direction(name=name)
    db.add(db_direction)
    db.commit()
    db.refresh(db_direction)
    return db_direction

def get_directions(db: Session):
    return db.query(Direction).all()

def get_direction(db: Session, direction_id: int):
    return db.query(Direction).filter(Direction.id == direction_id).first()

def update_direction(db: Session, direction_id: int, name: str):
    db_direction = get_direction(db, direction_id)
    if db_direction:
        db_direction.name = name
        db.commit()
        db.refresh(db_direction)
    return db_direction

def delete_direction(db: Session, direction_id: int):
    db_direction = get_direction(db, direction_id)
    if db_direction:
        db.delete(db_direction)
        db.commit()
    return db_direction
