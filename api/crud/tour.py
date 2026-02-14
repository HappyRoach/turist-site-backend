from sqlalchemy.orm import Session
from database.schemas.tour import Tour
from typing import Optional, List

def create_tour(db: Session, name: str, description: Optional[str], country: Optional[str],
                city: Optional[str], duration: Optional[int], operator: str, 
                price: Optional[float], image_url: Optional[str], external_url: str):
    db_tour = Tour(
        name=name,
        description=description,
        country=country,
        city=city,
        duration=duration,
        operator=operator,
        price=price,
        image_url=image_url,
        external_url=external_url
    )
    db.add(db_tour)
    db.commit()
    db.refresh(db_tour)
    return db_tour

def get_tours(db: Session, skip: int = 0, limit: int = 100, operator: Optional[str] = None):
    query = db.query(Tour)
    if operator:
        query = query.filter(Tour.operator == operator)
    return query.offset(skip).limit(limit).all()

def get_tour(db: Session, tour_id: int):
    return db.query(Tour).filter(Tour.id == tour_id).first()

def update_tour(db: Session, tour_id: int, **kwargs):
    db_tour = db.query(Tour).filter(Tour.id == tour_id).first()
    if db_tour:
        for key, value in kwargs.items():
            if value is not None:
                setattr(db_tour, key, value)
        db.commit()
        db.refresh(db_tour)
    return db_tour

def delete_tour(db: Session, tour_id: int):
    db_tour = db.query(Tour).filter(Tour.id == tour_id).first()
    if db_tour:
        db.delete(db_tour)
        db.commit()
    return db_tour
