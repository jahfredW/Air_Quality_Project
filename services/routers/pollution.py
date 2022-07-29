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


@router.get('/pollution/all')
async def read_all(db: Session = Depends(get_db)):
     pollution_model = db.query(api_create_models.Pollution).all()
     if pollution_model is not None:
         return pollution_model
     raise HTTPException(status_code=404, detail='Not Found')











