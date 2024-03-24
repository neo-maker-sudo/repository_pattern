from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.conf import settings


engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = session()

    try:
        yield db

    finally:
        db.close()
