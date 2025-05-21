#!/bin/bash

echo "Ожидание готовности базы данных..."
sleep 5

echo "Запуск миграций..."
python3 -m alembic upgrade head
if [ $? -ne 0 ]; then
    echo "Ошибка при выполнении миграций"
    exit 1
fi

echo "Инициализация базы данных..."
python3 init_db.py
if [ $? -ne 0 ]; then
    echo "Ошибка при инициализации базы данных"
    exit 1
fi

echo "Запуск приложения..."
python3 main.py
