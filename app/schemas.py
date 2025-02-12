from pydantic import BaseModel, EmailStr
from typing import Literal

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    role: Literal["admin", "tourist"]

class UserLogin(BaseModel):
    email: EmailStr
    password: str