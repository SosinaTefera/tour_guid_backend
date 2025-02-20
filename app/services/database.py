from sqlalchemy.engine import create_engine
from google.cloud import bigquery
from google.oauth2 import service_account
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

CREDENTIALS_PATH = os.getenv("CREDENTIALS_PATH")
credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_PATH)

PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_ID = os.getenv("DATASET_ID")


BIGQUERY_URI = f"bigquery://{PROJECT_ID}/{DATASET_ID}"

engine = create_engine(BIGQUERY_URI, credentials_path=CREDENTIALS_PATH)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
