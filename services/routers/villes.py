import sys
sys.path.append("..")

import api_create_models
from api_connect import engine, SessionLocal
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .auth import get_current_user, get_user_exception

router = APIRouter()

#api_create_models.Base.metadata.drop_all(bind=engine)
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
    if ville_query is not None:
        return ville_query
    raise HTTPException(status_code=404, detail='Not Found')


@router.get('/villes/{id_ville}')
async def read_ville_id(id_ville: str, db: Session = Depends(get_db)):
     pollution_model = db.query(api_create_models.Pollution).join(api_create_models.Ville).filter(api_create_models.Ville.nom == id_ville).all()
     if pollution_model is not None:
         return pollution_model
     raise HTTPException(status_code=404, detail='Not Found')


