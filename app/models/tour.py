from sqlalchemy import Column, String, Text, Float, DateTime
from app.services.database import Base
from sqlalchemy.orm import relationship




class Tour(Base):
    __tablename__ = "tours"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    image = Column(String, nullable=True)  
    price = Column(Float, nullable=False)
    created_at = Column(DateTime) 
    reviews = relationship("Review", back_populates="tour")  


