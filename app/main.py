from fastapi import FastAPI
from app.services.database import Base, engine
from app.routes import user

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix="/user", tags=["User"])



@app.get("/")
def read_root():
    return {"message": "Welcome to the Tour Guide API"}
