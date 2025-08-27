from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum as SQLAlchemyEnum
import enum
from .database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Role(str, enum.Enum):
    ADMIN = "admin"
    USER = "user"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    role = Column(SQLAlchemyEnum(Role))
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # Relacionamento com a classe Task
    tasks = relationship("Task", back_populates="assignee")


class TaskStatus(str, enum.Enum):
    COMPLETED = "completed"
    IN_PROGRESS = "in_progress"
    ON_HOLD = "on_hold"
    NOT_STARTED = "not_started"
    REVIEW = "review"

class TaskPriority(str, enum.Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    status = Column(SQLAlchemyEnum(TaskStatus))
    assignee_id = Column(Integer, ForeignKey("users.id"))
    due_date = Column(DateTime, server_default=func.now())
    priority = Column(SQLAlchemyEnum(TaskPriority))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())
    completed_at = Column(DateTime, nullable=True) # Should only be set when task is completed

    # Relacionamento com a classe User
    assignee = relationship("User", back_populates="tasks")
