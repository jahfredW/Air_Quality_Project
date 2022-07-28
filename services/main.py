from fastapi import FastAPI, Depends, HTTPException, APIRouter
from typing import Optional
import api_create_models
from api_connect import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field


app = FastAPI()

#api_create_models.Base.metadata.drop_all(bind=engine)
api_create_models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()