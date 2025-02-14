from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List
from app.schemas import TourUpdate, TourResponse
from app.models.tour import Tour
from app.services.database import get_db
from app.services.auth import get_current_user
from app.config import UPLOAD_DIR
import shutil
from datetime import datetime
import uuid


router = APIRouter()

# Get all tours (Both Admin and Tourist can access)
@router.get("/", response_model=List[TourResponse])
def get_tours(db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)  
):
    tours = db.query(Tour).all()
    return tours


# Create a tour (Admin only)
@router.post("/", response_model=TourResponse)
def create_tour(
    title: str = Form(...),
    description: str = Form(...),
    latitude: float = Form(...),
    longitude: float = Form(...),
    price: float = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admins only!")

    image_path = f"{UPLOAD_DIR}/{image.filename}"
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    new_tour = Tour(
        id=str(uuid.uuid4()),
        title=title,
        description=description,
        latitude=latitude,
        longitude=longitude,
        price=price,
        created_at=datetime.now(), 
        image=image_path  
    )

    db.add(new_tour)
    db.commit()
    db.refresh(new_tour)

    return new_tour

# Update a tour (Admin only)
@router.put("/{tour_id}", response_model=TourResponse)
def update_tour(
    tour_id: int,
    tour_data: TourUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admins only!")

    tour = db.query(Tour).filter(Tour.id == tour_id).first()
    if not tour:
        raise HTTPException(status_code=404, detail="Tour not found")
    
    for key, value in tour_data.dict().items():
        setattr(tour, key, value)
    
    db.commit()
    db.refresh(tour)
    return tour


# Delete a tour (Admin only)
@router.delete("/{tour_id}")
def delete_tour(
    tour_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admins only!")
    
    tour = db.query(Tour).filter(Tour.id == tour_id).first()
    if not tour:
        raise HTTPException(status_code=404, detail="Tour not found")

    db.delete(tour)
    db.commit()
    return {"message": "Tour deleted successfully"}
