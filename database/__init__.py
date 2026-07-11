from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from setting import DATABASE_URL

Base = declarative_base()
connect_args = {}
if DATABASE_URL.startswith("postgresql"):
    connect_args = {
        'client_encoding': 'utf8',
        'options': '-c client_encoding=utf8'
    }

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args=connect_args
)
Session = sessionmaker(bind=engine)
