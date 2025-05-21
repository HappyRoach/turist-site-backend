from database import Session
from api.crud.role import create_role, get_role
from api.crud.user import create_user, get_user_by_login
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
        try:
            existing_role = get_role(db, role["id"])
            if not existing_role:
                create_role(db, role["name"])
                print(f"Роль '{role['name']}' успешно создана")
        except Exception as e:
            print(f"Ошибка при обработке роли '{role['name']}': {e}")

def init_superadmin(db: Session):
    """Инициализация суперпользователя"""
    try:
        existing_user = get_user_by_login(db, SUPERADMIN_LOGIN)
        if not existing_user:
            user = User()
            hashed_password = user.set_password(SUPERADMIN_PASSWORD)
            create_user(
                db=db,
                login=SUPERADMIN_LOGIN,
                password=hashed_password,
                role_id=3
            )
            print("Суперпользователь успешно создан")
    except Exception as e:
        print(f"Ошибка при создании суперпользователя: {e}")

def init_database():
    """Основная функция инициализации базы данных"""
    db = Session()
    try:
        print("Начало инициализации базы данных...")
        init_roles(db)
        init_superadmin(db)
        print("Инициализация базы данных успешно завершена")
    except Exception as e:
        print(f"Критическая ошибка при инициализации базы данных: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_database()
