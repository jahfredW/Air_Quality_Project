import json

from fastapi import FastAPI, Depends, HTTPException
import api_create_models
from api_connect import engine, SessionLocal
from sqlalchemy.orm import Session
from auth import CreateUser

app = FastAPI()

#api_create_models.Base.metadata.drop_all(bind=engine)
api_create_models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

"""
@app.get('/{id_ville}')
async def read_database(id_ville: str, db: Session = Depends(get_db)):
     pollution_model = db.query(api_create_models.Pollution).join(api_create_models.Ville).filter(api_create_models.Ville.nom == id_ville).all()
     if pollution_model is not None:
         print(type(pollution_model))
         data = {}
         data['data'] = pollution_model
         return data
     raise HTTPException(status_code=404, detail='Not Found')
"""
@app.get('/')
async def read_all(db: Session = Depends(get_db)):
     pollution_model = db.query(api_create_models.Pollution).all()
     if pollution_model is not None:
         return pollution_model
     raise HTTPException(status_code=404, detail='Not Found')

@app.post("/create/user")
async def create_new_user(create_user: CreateUser):
    create_user_model = api_create_models.User()
    create_user_model.email = create_user.email
    create_user_model.username = create_user.username
    create_user_model.first_name = create_user.first_name
    create_user_model.last_name = create_user.last_name
    create_user_model.hashed_password = create_user.password
    create_user_model.is_active = True

    return create_user_model