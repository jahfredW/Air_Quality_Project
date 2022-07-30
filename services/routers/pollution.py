import sys
sys.path.append("..")
import requests
import api_create_models
from api_connect import engine, SessionLocal
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .auth import get_current_user, get_user_exception
import requests
import pyowm
from pyowm.utils.config import get_default_config


router = APIRouter(
    prefix="/pollution",
    tags=["pollution"],
    responses={404: {"description": "Not found"}}
)

#api_create_models.Base.metadata.drop_all(bind=engine)
api_create_models.Base.metadata.create_all(bind=engine)



def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get('/all')
async def read_all(db: Session = Depends(get_db)):
     pollution_model = db.query(api_create_models.Pollution).all()
     if pollution_model is not None:
         return pollution_model
     else:
        raise HTTPException(status_code=404, detail='Not Found')


@router.get('/{id_pollution}')
async def read_all(id_pollution: int, db: Session = Depends(get_db)):
     pollution_model = db.query(api_create_models.Pollution).filter(api_create_models.Pollution.id_pollution == id_pollution).first()
     if pollution_model is not None:
         return pollution_model
     else:
        raise HTTPException(status_code=404, detail='Not Found')









