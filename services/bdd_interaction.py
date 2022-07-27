import json
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import FastAPI, Depends, HTTPException
import api_create_models
from api_connect import engine, SessionLocal
from sqlalchemy.orm import Session
from auth import CreateUser, get_hash_password
from fastapi.security import OAuth2PasswordRequestForm
from auth import authenticate_user, create_access_token, oauth2_bearer, SECRET_KEY, ALGO
from custom_except import get_user_exception, token_exception



app = FastAPI()

#api_create_models.Base.metadata.drop_all(bind=engine)
api_create_models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get('/{id_ville}')
async def read_database(id_ville: str, db: Session = Depends(get_db)):
     pollution_model = db.query(api_create_models.Pollution).join(api_create_models.Ville).filter(api_create_models.Ville.nom == id_ville).all()
     if pollution_model is not None:
         return pollution_model
     raise HTTPException(status_code=404, detail='Not Found')


@app.get('/')
async def read_all(db: Session = Depends(get_db)):
     pollution_model = db.query(api_create_models.Pollution).all()
     if pollution_model is not None:
         return pollution_model
     raise HTTPException(status_code=404, detail='Not Found')


async def get_current_user(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGO])
        username: str = payload.get("sub")
        id_user: int = payload.get("id")
        if username is None or id_user is None:
            raise get_user_exception()
        return {"username" : username, "id": id_user}
    except JWTError:
        raise get_user_exception()


@app.post("/create/user")
async def create_new_user(create_user: CreateUser, db: Session = Depends(get_db)):
    create_user_model = api_create_models.User()
    create_user_model.email = create_user.email
    create_user_model.username = create_user.username
    create_user_model.first_name = create_user.first_name
    create_user_model.last_name = create_user.last_name
    hash_password = get_hash_password(create_user.password)
    create_user_model.hashed_password = hash_password
    create_user_model.is_active = True

    try:
        db.add(create_user_model)
        db.commit()
    except Exception as e:
        print(e)
    return create_user_model


@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise token_exception()
    token_expires = timedelta(minutes=20)
    token = create_access_token(user.username,
                                user.id_user,
                                expires_delta=token_expires)
    return {"token" : token}

