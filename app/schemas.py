from pydantic import BaseModel, EmailStr
from typing import Literal
from datetime import datetime


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    role: Literal["admin", "tourist"]

class UserLogin(BaseModel):
    email: EmailStr
    password: str



# Tour
class TourBase(BaseModel):
    title: str
    description: str
    latitude: float
    longitude: float
    image: str  
    price: float
    created_at: datetime

class TourCreate(TourBase):
    pass  

class TourUpdate(TourBase):
    pass  

class TourResponse(TourBase):
    id: str

    class Config:
        from_attributes = True
