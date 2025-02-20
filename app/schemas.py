from pydantic import BaseModel, EmailStr
from typing import Literal, List, Optional
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


# Review
class ReviewCreate(BaseModel):
    comment: str
    rating: float
    tour_id: str

class ReviewResponse(BaseModel):
    id: str
    comment: str
    rating: float
    user_id: str
    created_at: datetime
    tour_id: str


# Tour
class TourBase(BaseModel):
    title: str
    description: str
    latitude: float
    longitude: float
    image: str  
    price: float
    created_at: datetime
    reviews: List[ReviewResponse] = []  


class TourCreate(TourBase):
    pass  

class TourUpdate(TourBase):
    pass  

class TourResponse(TourBase):
    id: str

    class Config:
        from_attributes = True


# User Profile
class UserProfileResponse(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: EmailStr
    role: str

    # class Config:
    #     from_attributes = True  

class UserProfileUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
