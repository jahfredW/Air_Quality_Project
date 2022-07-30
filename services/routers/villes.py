import sys

sys.path.append("..")
import datetime
import api_create_models
from api_connect import engine, SessionLocal
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from api_create_models import Ville
from fastapi.security import OAuth2PasswordRequestForm
from .auth import get_current_user, get_user_exception


class Create_ville(BaseModel):
    id_ville: int



router = APIRouter()

# api_create_models.Base.metadata.drop_all(bind=engine)
api_create_models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get('/villes/all')
def get_all_villes(db: Session = Depends(get_db)):
    ville_query = db.query(api_create_models.Ville).all()
    try:
        if ville_query is not None:
            return ville_query
    except TimeoutError as e:
        raise e
    raise HTTPException(status_code=404, detail='Not Found')


@router.get('/villes/{id_ville}')
async def read_ville_id(id_ville: int, db: Session = Depends(get_db)):
    ville_query = db.query(api_create_models.Ville).filter(api_create_models.Ville.id_ville == id_ville).first()
    if ville_query is not None:
        return ville_query
    raise HTTPException(status_code=404, detail='Not Found')


@router.post('/villes/')
async def read_ville_id(form: Create_ville, db: Session = Depends(get_db)):
    ville_model = Ville()
    ville_model.id_ville = form.id_ville

    ville_query = db.query(api_create_models.Ville).filter(api_create_models.Ville.id_ville == form.id_ville).first()
    if ville_query is not None:
        return ville_query
    raise HTTPException(status_code=404, detail='Not Found')