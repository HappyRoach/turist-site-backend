import os

SECRET_KEY = os.getenv('SECRET_KEY', 'cKpBOnozxE5Be4Th4AAtWi0jTcIyw+SFt9pqVMTmrww=')  # openssl rand -base64 32

DATABASE_URL = os.getenv('DATABASE_URL', "postgresql://postgres:rt25pcx501@localhost:5432/postgres")

SUPERADMIN_LOGIN = os.getenv('SUPERADMIN_LOGIN', 'ADMIN')
SUPERADMIN_PASSWORD = os.getenv('SUPERADMIN_PASSWORD', 'ADMIN')
