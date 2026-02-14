from pydantic import BaseModel, Field, HttpUrl
from typing import Optional

class TourBase(BaseModel):
    name: str = Field(..., description="Название тура")
    description: Optional[str] = Field(None, description="Краткое описание")
    country: Optional[str] = Field(None, description="Страна")
    city: Optional[str] = Field(None, description="Город")
    duration: Optional[int] = Field(None, description="Длительность в днях")
    operator: str = Field(..., description="Туроператор: Золотой глобус или Фейерверк")
    price: Optional[float] = Field(None, description="Цена тура")
    image_url: Optional[str] = Field(None, description="URL изображения")
    external_url: str = Field(..., description="Ссылка на страницу тура на сайте туроператора")

class TourCreate(TourBase):
    pass

class TourUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    duration: Optional[int] = None
    operator: Optional[str] = None
    price: Optional[float] = None
    image_url: Optional[str] = None
    external_url: Optional[str] = None

class Tour(TourBase):
    id: int

    class Config:
        from_attributes = True
