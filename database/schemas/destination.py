from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum

from ..utils.database import Base

class ActivityType(str, enum.Enum):
    ACTIVE = "active"
    CALM = "calm"
    CULTURAL = "cultural"
    FOOD = "food"

class ClimateType(str, enum.Enum):
    COLD = "cold"
    WARM = "warm"
    MODERATE = "moderate"

class LengthType(str, enum.Enum):
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"

class TransportType(str, enum.Enum):
    PLANE = "plane"
    TRAIN = "train"
    CAR = "car"
    SHIP = "ship"

class BudgetType(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Destination(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True, index=True)
    activity = Column(Enum(ActivityType), nullable=False)
    climate = Column(Enum(ClimateType), nullable=False)
    length = Column(Enum(LengthType), nullable=False)
    transport = Column(Enum(TransportType), nullable=False)
    budget = Column(Enum(BudgetType), nullable=False)
    result = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="destinations")

    def __repr__(self):
        return f"<Destination(id='{self.id}', activity='{self.activity}', climate='{self.climate}', length='{self.length}', transport='{self.transport}', budget='{self.budget}', user_id='{self.user_id}')>"