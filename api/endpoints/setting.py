from fastapi import APIRouter, Depends, HTTPException, status
from .. import crud, security
from ..schemas.setting import Setting, SettingCreate, AdminPasswordChange
from ..utils.database import get_db, Session
from database.schemas.user import User

router = APIRouter()

@router.get("/{key}", response_model=Setting)
def get_setting(key: str, db: Session = Depends(get_db)):
    setting = crud.get_setting(db, key=key)
    if not setting:
        return {"key": key, "value": ""}
    return setting

@router.post("/", response_model=Setting)
def save_setting(
    setting: SettingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(security.check_role(["superadmin", "admin"]))
):
    return crud.save_setting(db, key=setting.key, value=setting.value)

@router.post("/change-password")
def change_password(
    data: AdminPasswordChange,
    db: Session = Depends(get_db),
    current_user: User = Depends(security.check_role(["superadmin", "admin"]))
):
    success = crud.update_admin_password(
        db, 
        user_id=current_user.id, 
        current_pw=data.current_password, 
        new_pw=data.new_password
    )
    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect current password"
        )
    return {"message": "Password changed successfully"}
