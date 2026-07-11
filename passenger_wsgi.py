import sys
import os

# Добавляем пути к виртуальному окружению Python на Beget
# Beget автоматически создает venv в корне приложения
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'venv', 'lib', 'python3.12', 'site-packages'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'venv', 'lib', 'python3.11', 'site-packages'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'venv', 'lib', 'python3.10', 'site-packages'))
sys.path.insert(0, os.path.dirname(__file__))

from main import app
from a2wsgi import ASGIMiddleware

# Passenger WSGI сервер ожидает переменную "application"
application = ASGIMiddleware(app)
