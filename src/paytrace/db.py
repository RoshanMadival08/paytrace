from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

#DATABASE_URL = "postgresql+psycopg://paytrace:paytrace@localhost:5432/paytrace"

DATABASE_URL = "postgresql+psycopg://paytrace:paytrace@127.0.0.1:5432/paytrace"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()