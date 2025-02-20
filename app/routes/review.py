from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas import ReviewCreate, ReviewResponse
from app.models.tour import Tour
from app.models.review import Review
from app.models.user import User
from app.services.database import get_db
from app.services.auth import get_current_user
from datetime import datetime
import uuid

router = APIRouter()

# Create a review for a tour
@router.post("/", response_model=ReviewResponse)
def create_review(
    review: ReviewCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    tour = db.query(Tour).filter(Tour.id == review.tour_id).first()
    if not tour:
        raise HTTPException(status_code=404, detail="Tour not found")

    new_review = Review(
        id=str(uuid.uuid4()),
        comment=review.comment,
        rating=review.rating,
        user_id=current_user["id"],
        created_at=datetime.now(), 
        tour_id=review.tour_id
    )
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review


# Get all reviews for a tour
@router.get("/", response_model=List[ReviewResponse])
def get_reviews_for_tour(
    tour_id: int,
    db: Session = Depends(get_db)
):
    tour = db.query(Tour).filter(Tour.id == tour_id).first()
    if not tour:
        raise HTTPException(status_code=404, detail="Tour not found")

    reviews = db.query(Review).filter(Review.tour_id == tour_id).all()
    return reviews