from sqlalchemy import Column, String
from .. import Base

class Setting(Base):
    __tablename__ = 'settings'

    key = Column(String(100), primary_key=True, index=True)
    value = Column(String(1000), nullable=True)

    def __repr__(self):
        return f"<Setting(key='{self.key}', value='{self.value}')>"
