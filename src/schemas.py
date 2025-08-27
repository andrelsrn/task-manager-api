from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    role: str
    email: EmailStr
    password: str

class User(BaseModel):
    id: int
    name: str
    role: str
    email: EmailStr

    class Config:
        orm_mode = True