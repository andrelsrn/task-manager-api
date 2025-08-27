from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Using a path relative to the project root is more stable than relative to the CWD (./)
SQLALCHEMY_DATABASE_URL = "sqlite:///task_manager.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# New SQLAlchemy 2.0 declarative base
class Base(DeclarativeBase):
    pass

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()