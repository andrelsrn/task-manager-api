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
