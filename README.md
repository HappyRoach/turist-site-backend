# Where? - Туристический сайт (Backend)

## Описание проекта
Backend часть туристического веб-приложения, разработанного с использованием FastAPI и PostgreSQL.

## Технологии
- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- JWT для аутентификации
- Alembic для миграций

## Требования
- Docker и Docker Compose
- Python 3.12 (для локальной разработки)

## Установка и запуск

### Использование Docker
1. Клонируйте репозиторий:
```bash
git clone [url-репозитория]
cd turist-site-backend
```

2. Запустите приложение с помощью Docker Compose:
```bash
docker-compose up --build
```

Приложение будет доступно по адресу: `http://localhost:9667`

### Локальная разработка
1. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Настройте переменные окружения:
- DATABASE_URL
- SECRET_KEY

4. Примените миграции базы данных:
```bash
alembic upgrade head
```

5. Запустите приложение:
```bash
python main.py
```

## Миграции базы данных
Проект использует Alembic для управления миграциями базы данных. Основные команды:

```bash
# Создать новую миграцию
alembic revision --autogenerate -m "описание изменений"

# Применить все миграции
alembic upgrade head

# Откатить последнюю миграцию
alembic downgrade -1

# Показать текущую версию
alembic current
```

## API Endpoints
API доступно по адресу: `http://localhost:9667`

Документация API доступна через:
- Swagger UI: `http://localhost:9667/docs`
- ReDoc: `http://localhost:9667/redoc`

## База данных
Проект использует PostgreSQL. Настройки подключения:
- Хост: localhost
- Порт: 5432
- База данных: postgres
- Пользователь: postgres
- Пароль: rt25pcx501

## Безопасность
- Используется JWT для аутентификации
- Пароли хешируются с помощью bcrypt
- CORS настроен для безопасного взаимодействия с фронтендом
