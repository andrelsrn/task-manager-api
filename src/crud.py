from src.models import User, Task, Role, TaskStatus, TaskPriority
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from . import models
from . import schemas
from .auth import get_password_hash

# ----- Usuários -----

# Buscar usuario pelo ID
def get_user(user_id: int, db: Session):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(..., hashed_password=hashed_password)
    return db.query(User).filter(User.id == user_id).first()


# Listar todos usuarios
def get_users(db: Session):
    return db.query(User).all()


# Criar usuario
def create_user(user: schemas.UserCreate, db: Session):
    db_user = User(name=user.name, role=user.role,
                   email=user.email, hashed_password=user.hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Atualizar usuario
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
