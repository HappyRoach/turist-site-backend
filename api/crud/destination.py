from sqlalchemy.orm import Session
from ..utils.destinations import TouristDestinations
from database.schemas.destination import Destination, ActivityType, ClimateType, LengthType, TransportType, BudgetType

def create_destination(db: Session, activity: ActivityType, climate: ClimateType, length: LengthType, 
                      transport: TransportType, budget: BudgetType, user_id: int):
    destinations = TouristDestinations(activity.value, climate.value, length.value, transport.value, budget.value)
    result = destinations.get_destinations()
    
    db_destination = Destination(
        activity=activity,
        climate=climate,
        length=length,
        transport=transport,
        budget=budget,
        result=str(result),
        user_id=user_id
    )
    db.add(db_destination)
    db.commit()
    db.refresh(db_destination)
    return db_destination, result

def get_destinations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Destination).offset(skip).limit(limit).all()

def get_user_destinations(db: Session, user_id: int):
    return db.query(Destination).filter(Destination.user_id == user_id).all()

def get_destination(db: Session, destination_id: int):
    return db.query(Destination).filter(Destination.id == destination_id).first()

def delete_destination(db: Session, destination_id: int):
    destination = db.query(Destination).filter(Destination.id == destination_id).first()
    if destination:
        db.delete(destination)
        db.commit()
    return destination 