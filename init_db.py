from database import Session
from api.crud.role import create_role, get_role
from api.crud.user import create_user, get_user
from database.schemas.user import User
from setting import SUPERADMIN_LOGIN, SUPERADMIN_PASSWORD

def init_roles(db: Session):
    """Инициализация ролей в базе данных"""
    roles = [
        {"id": 1, "name": "user"},
        {"id": 2, "name": "admin"},
        {"id": 3, "name": "superadmin"}
    ]
    
    for role in roles:
        existing_role = get_role(db, role["id"])
        if not existing_role:
            create_role(db, role["name"])

def init_superadmin(db: Session):
    """Инициализация суперпользователя"""
    existing_user = get_user(db, 0)
    if not existing_user:
        user = User()
        hashed_password = user.set_password(SUPERADMIN_PASSWORD)
        create_user(
            db=db,
            login=SUPERADMIN_LOGIN,
            password=hashed_password,
            role_id=4
        )

def init_database():
    """Основная функция инициализации базы данных"""
    db = Session()
    try:
        init_roles(db)
        init_superadmin(db)
        print("База данных успешно инициализирована")
    except Exception as e:
        print(f"Ошибка при инициализации базы данных: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    init_database()
