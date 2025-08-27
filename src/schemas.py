from pydantic import BaseModel, EmailStr
from datetime import datetime
from src.models import Role, TaskStatus, TaskPriority
from typing import Optional

# ===================
# Schemas para User
# ===================

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: Role

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[Role] = None
    password: Optional[str] = None

# ===================
# Schemas para Task
# ===================

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    status: TaskStatus = TaskStatus.NOT_STARTED
    priority: TaskPriority = TaskPriority.MEDIUM
    due_date: datetime | None = None

class TaskCreate(TaskBase):
    assignee_id: int

class Task(TaskBase):
    id: int
    created_at: datetime
    assignee: User # Para mostrar o usuário completo ao invés de só o ID

    class Config:
        from_attributes = True

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    due_date: Optional[datetime] = None

# ===================
# Schema para Relações
# ===================

class UserWithTasks(User):
    tasks: list[Task] = []
