from fastapi import FastAPI
from app.services.database import Base, engine
from app.routes import user, tour, review,vizualization


app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(tour.router, prefix="/tour", tags=["Tour"])
app.include_router(review.router, prefix="/review", tags=["Review"])
app.include_router(vizualization.router, prefix="/vizualization", tags=["Vizualization"])




@app.get("/")
def read_root():
    return {"message": "Welcome to the Tour Guide API"}
