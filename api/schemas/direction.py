from pydantic import BaseModel, Field

class DirectionBase(BaseModel):
    name: str = Field(..., description="Название направления")

class DirectionCreate(DirectionBase):
    pass

class DirectionUpdate(DirectionBase):
    pass

class Direction(DirectionBase):
    id: int

    class Config:
        from_attributes = True
