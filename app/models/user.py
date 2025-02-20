from sqlalchemy import Column, String, Enum
from app.services.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum("admin", "tourist", name="user_roles"), nullable=False)
    reviews = relationship("Review", back_populates="user")

