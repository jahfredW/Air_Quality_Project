import sys
sys.path.append("..")
import requests
import api_create_models
import geopy
from api_connect import engine, SessionLocal
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .auth import get_current_user, get_user_exception
from business.components.pollution_ville import PollutionVille
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
         print(pollution_model)
         return pollution_model
     else:
        raise HTTPException(status_code=404, detail='Not Found')


@router.get('/{nom_ville}')
async def read_all(nom_ville: str, db: Session = Depends(get_db)):
     pollution_model = db.query(api_create_models.Pollution)\
         .join(api_create_models.Ville)\
         .filter(api_create_models.Ville.nom == nom_ville)\
         .first()
     if pollution_model is not None:
         print('lecture bdd pour : {0}'.format(pollution_model))
         return pollution_model
     else:
         loc = geopy.geocoders.Nominatim(user_agent="GetLoc")
         getLoc = loc.geocode(nom_ville)
         r = requests.get(f'http://api.openweathermap.org/data/2.5/air_pollution?lat={getLoc.latitude}&lon={getLoc.longitude}&appid=a1f0eace01a7421a3046c32bf90392a5')
         texte = r.json()
         return texte














