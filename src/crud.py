from src.models import User, Task, Role, TaskStatus, TaskPriority
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from . import models
from . import schemas
from .auth import get_password_hash


# ----- Usuários -----

# Buscar usuario pelo ID
def get_user(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(email: str, db: Session):
    return db.query(models.User).filter(models.User.email == email).first()


# Listar todos usuarios
def get_users(db: Session):
    return db.query(User).all()


# Criar usuario
def create_user(user: schemas.UserCreate, db: Session):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(name=user.name, role=user.role,
                   email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Atualizar usuario
def update_user(user_id: int, user: schemas.UserUpdate, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    
    # Get the update data, excluding unset fields
    update_data = user.model_dump(exclude_unset=True)

    # Hash the password if it's being updated
    if "password" in update_data and update_data["password"] is not None:
        hashed_password = get_password_hash(update_data["password"])
        update_data["hashed_password"] = hashed_password
        del update_data["password"] # Don't try to set a 'password' attribute on the model

    for key, value in update_data.items():
        setattr(db_user, key, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user


# Deletar usuario
def delete_user(user_id: int, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user


# ----- Tarefas -----

# Criar tarefa
def create_task(task: schemas.TaskCreate, db: Session):
    db_task = models.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Buscar tarefa pelo ID
def get_task(task_id: int, db: Session):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

# Listar todas as tarefas
def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()

# Atualizar tarefa
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        return None
    
    update_data = task.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)
    
    db.commit()
    db.refresh(db_task)
    return db_task

# Deletar tarefa
def delete_task(task_id: int, db: Session):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task