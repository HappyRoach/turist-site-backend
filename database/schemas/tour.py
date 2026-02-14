from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.orm import relationship

from .. import Base

class Tour(Base):
    __tablename__ = 'tours'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    country = Column(String(100))
    city = Column(String(100))
    duration = Column(Integer)  
    operator = Column(String(50), nullable=False) 
    price = Column(Float, nullable=True)
    image_url = Column(String(500))
    external_url = Column(String(500), nullable=False)  # ссылка на сайт туроператора

    def __repr__(self):
        return f"<Tour(name='{self.name}', operator='{self.operator}', id='{self.id}')>"
    