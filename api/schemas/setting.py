from pydantic import BaseModel, Field
from typing import Optional

class SettingBase(BaseModel):
    key: str = Field(..., description="Ключ настройки")
    value: Optional[str] = Field(None, description="Значение настройки")

class SettingCreate(SettingBase):
    pass

class Setting(SettingBase):
    class Config:
        from_attributes = True

class AdminPasswordChange(BaseModel):
    current_password: str = Field(..., description="Текущий пароль")
    new_password: str = Field(..., description="Новый пароль")
