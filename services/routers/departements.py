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


@router.get('/departements/all')
async def get_all_departements(db: Session = Depends(get_db)):
    dep = db.query(api_create_models.Departement).all()
    if dep is not None:
        return dep
    else:
        raise HTTPException(status_code=404, detail='Not found')
