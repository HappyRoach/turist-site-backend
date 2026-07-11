from database import Session, Base, engine
import database.schemas
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

from api import crud
from database.schemas.direction import Direction
from database.schemas.survey import SurveyQuestion
from database.schemas.setting import Setting

def init_directions(db: Session):
    default_dirs = ['Развлекательные', 'По России', 'За границей', 'Приключения', 'Экскурсионные', 'Пляжные']
    for name in default_dirs:
        try:
            existing = db.query(Direction).filter(Direction.name == name).first()
            if not existing:
                crud.create_direction(db, name=name)
                print(f"Направление '{name}' создано")
        except Exception as e:
            print(f"Ошибка при создании направления '{name}': {e}")

def init_survey(db: Session):
    try:
        existing = db.query(SurveyQuestion).first()
        if not existing:
            q = crud.create_question(db, title="Какой курортный район предпочитаете?")
            crud.add_answer(db, question_id=q.id, text="Шумный и молодёжный, с клубами", criterion="Развлекательность", score=2)
            crud.add_answer(db, question_id=q.id, text="Спокойный, семейный", criterion="Развлекательность", score=8)
            crud.add_answer(db, question_id=q.id, text="Уединенный, элитный", criterion="Развлекательность", score=6)
            print("Начальный опрос создан")
    except Exception as e:
        print(f"Ошибка при создании опроса: {e}")

def init_settings(db: Session):
    try:
        existing = db.query(Setting).filter(Setting.key == 'admin_panel_title').first()
        if not existing:
            crud.save_setting(db, key='admin_panel_title', value='Тур Админ')
            print("Настройка названия админки создана")
    except Exception as e:
        print(f"Ошибка при создании настроек: {e}")

def init_database():
    """Основная функция инициализации базы данных"""
    print("Создание таблиц в базе данных...")
    Base.metadata.create_all(bind=engine)
    db = Session()
    try:
        print("Начало инициализации базы данных...")
        init_roles(db)
        init_superadmin(db)
        init_directions(db)
        init_survey(db)
        init_settings(db)
        print("Инициализация базы данных успешно завершена")
    except Exception as e:
        print(f"Критическая ошибка при инициализации базы данных: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_database()
