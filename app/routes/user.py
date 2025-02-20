from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.database import get_db
from app.models.user import User
from app.schemas import UserCreate, UserLogin, UserProfileResponse, UserProfileUpdate
from app.services.auth import hash_password, verify_password, create_access_token, get_current_user
import uuid


router = APIRouter()

@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        id=str(uuid.uuid4()),
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_access_token({"sub": db_user.email, "role": db_user.role, "id":db_user.id,"first_name":db_user.first_name, "last_name":db_user.last_name})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/profile", response_model=UserProfileResponse)
def get_profile(current_user: User = Depends(get_current_user),db: Session = Depends(get_db),):
    user_id = current_user['id']
    user = db.query(User).filter(User.id == user_id).first()

    return user


@router.put("/profile", response_model=UserProfileResponse)
def update_profile(
    update_data: UserProfileUpdate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    user_id = current_user['id']
    user = db.query(User).filter(User.id == user_id).first()
    if update_data.first_name:
        user.first_name = update_data.first_name
    if update_data.last_name:
        user.last_name = update_data.last_name
   
    db.commit()
    db.refresh(user)
    
    return user