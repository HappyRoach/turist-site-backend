from pydantic import BaseModel, Field
from typing import Optional, List, Tuple
from enum import Enum

class ActivityType(str, Enum):
    ACTIVE = "active"
    CALM = "calm"
    CULTURAL = "cultural"
    FOOD = "food"

class ClimateType(str, Enum):
    COLD = "cold"
    WARM = "warm"
    MODERATE = "moderate"

class LengthType(str, Enum):
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"

class TransportType(str, Enum):
    PLANE = "plane"
    TRAIN = "train"
    CAR = "car"
    SHIP = "ship"

class BudgetType(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class DestinationBase(BaseModel):
    activity: ActivityType = Field(..., description="Тип активности: active, calm, cultural, food")
    climate: ClimateType = Field(..., description="Тип климата: cold, warm, moderate")
    length: LengthType = Field(..., description="Длительность: short, medium, long")
    transport: TransportType = Field(..., description="Тип транспорта: plane, train, car, ship")
    budget: BudgetType = Field(..., description="Бюджет: low, medium, high")

class DestinationCreate(DestinationBase):
    pass

class DestinationResult(BaseModel):
    destinations: List[Tuple[str, float]]

class Destination(DestinationBase):
    id: int
    user_id: int
    result: str

    class Config:
        from_attributes = True 