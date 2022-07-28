import json
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import FastAPI
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from auth import authenticate_user, create_access_token, oauth2_bearer, get_hash_password, SessionLocal, \
    Key, get_user_exception, token_exception, User, CreateUser




router = APIRouter()

app = FastAPI()
app.include_router(router)


#api_create_models.Base.metadata.drop_all(bind=engine)
#api_create_models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

"""
@router.get('/{id_ville}')
async def read_database(id_ville: str, db: Session = Depends(get_db)):
     pollution_model = db.query(api_create_models.Pollution).join(api_create_models.Ville).filter(api_create_models.Ville.nom == id_ville).all()
     if pollution_model is not None:
         return pollution_model
     raise HTTPException(status_code=404, detail='Not Found')


@router.get('/')
async def read_all(db: Session = Depends(get_db)):
     pollution_model = db.query(api_create_models.Pollution).all()
     if pollution_model is not None:
         return pollution_model
     raise HTTPException(status_code=404, detail='Not Found')
"""



