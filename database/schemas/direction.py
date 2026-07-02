from sqlalchemy import Column, Integer, String
from .. import Base

class Direction(Base):
    __tablename__ = 'directions'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False, unique=True)

    def __repr__(self):
        return f"<Direction(name='{self.name}', id='{self.id}')>"
