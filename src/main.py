from fastapi import FastAPI, Depends, HTTPException
from . import models, schemas, crud
from .database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Welcome to the Task Manager API!"}

# Criar usuario


@app.post("/users/", response_model=schemas.User)
def create_user_endpoint(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(email=user.email, db=db)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(user=user, db=db)


# ----- Endpoints de Usuários -----

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(skip=skip, limit=limit, db=db)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(user_id=user_id, db=db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}", response_model=schemas.User)
def update_user_endpoint(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.update_user(user_id=user_id, user=user, db=db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_id}")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(user_id=user_id, db=db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}


# ----- Endpoints de Tarefas -----

@app.post("/tasks/", response_model=schemas.Task)
def create_task_endpoint(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    # Check if assignee_id exists
    assignee = crud.get_user(user_id=task.assignee_id, db=db)
    if not assignee:
        raise HTTPException(status_code=400, detail="Assignee user not found")
    return crud.create_task(task=task, db=db)

@app.get("/tasks/", response_model=list[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(skip=skip, limit=limit, db=db)
    return tasks

@app.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(task_id=task_id, db=db)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task_endpoint(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = crud.update_task(task_id=task_id, task=task, db=db)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.delete_task(task_id=task_id, db=db)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
