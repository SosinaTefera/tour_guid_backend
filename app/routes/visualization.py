from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.database import get_db
from app.services.auth import get_current_user
from app.models.tour import Tour


router = APIRouter()

@router.get("/tours-over-time")
def tours_over_time(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admins only!")

    tours = db.query(Tour).all()

    tours_by_date = {}
    for tour in tours:
        date = tour.created_at.date()  
        tours_by_date[date] = tours_by_date.get(date, 0) + 1

    sorted_dates = sorted(tours_by_date.keys())
    counts = [tours_by_date[date] for date in sorted_dates]

    return {
        "labels": [str(date) for date in sorted_dates], 
        "data": counts 
    }

@router.get("/reviews-per-tour")
def reviews_per_tour(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admins only!")

    tours = db.query(Tour).all()

    tour_titles = [tour.title for tour in tours]
    review_counts = [len(tour.reviews) for tour in tours]

    return {
        "labels": tour_titles,  
        "data": review_counts  
    }

    

@router.get("/average-ratings")
def average_ratings(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admins only!")

    tours = db.query(Tour).all()

    tour_titles = [tour.title for tour in tours]
    avg_ratings = []

    for tour in tours:
        if tour.reviews:
            avg_rating = sum(review.rating for review in tour.reviews) / len(tour.reviews)
            avg_ratings.append(avg_rating)
        else:
            avg_ratings.append(0)  # No reviews

    return {
        "labels": tour_titles,  
        "data": avg_ratings  
    }

    
@router.get("/revenue")
def revenue(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admins only!")

    tours = db.query(Tour).all()
    tour_titles = [tour.title for tour in tours]
    revenue = [tour.price * len(tour.bookings) for tour in tours]  

    return {
        "labels": tour_titles,  
        "data": revenue 
    }