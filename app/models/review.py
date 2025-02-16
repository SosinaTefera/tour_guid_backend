from sqlalchemy import Column, String, Text, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.services.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(String, primary_key=True)
    comment = Column(Text, nullable=False)
    rating = Column(Float, nullable=False)  
    user_id = Column(String, ForeignKey("users.id"), nullable=False)  
    tour_id = Column(String, ForeignKey("tours.id"), nullable=False)  
    created_at = Column(DateTime) 

    
    # Relationships
    user = relationship("User", back_populates="reviews") 
    tour = relationship("Tour", back_populates="reviews")  