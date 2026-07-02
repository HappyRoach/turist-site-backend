from sqlalchemy.orm import Session
from database.schemas.setting import Setting
from database.schemas.user import User
from typing import Optional

def get_setting(db: Session, key: str):
    return db.query(Setting).filter(Setting.key == key).first()

def save_setting(db: Session, key: str, value: str):
    db_setting = get_setting(db, key)
    if not db_setting:
        db_setting = Setting(key=key, value=value)
        db.add(db_setting)
    else:
        db_setting.value = value
    db.commit()
    db.refresh(db_setting)
    return db_setting

def update_admin_password(db: Session, user_id: int, current_pw: str, new_pw: str) -> bool:
    user = db.query(User).filter(User.id == user_id).first()
    if user and user.verify_password(current_pw):
        user.set_password(new_pw)
        db.commit()
        return True
    return False
