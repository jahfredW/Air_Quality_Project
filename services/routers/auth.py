import sys

sys.path.append("..")

from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI,Depends, HTTPException, status, APIRouter
from datetime import datetime, timedelta
from passlib.context import CryptContext
from api_connect import SessionLocal, engine
import api_create_models
from api_create_models import User
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated='auto')

api_create_models.Base.metadata.create_all(bind=engine)

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "oizejdoùzed9+4z5e+d9zedjzoih"
ALGO = "HS256"


class CreateUser(BaseModel):
    """
    class simplfié hérite de Basemodel
    permet de définir le model de formulaire basé sur la classe USER
    """
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str


router = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_hash_password(password):
    """
    Permet d'obtenir un mot de pass crypté ( JWT )
    :param password:
    :return: Le mote de passe crypté
    """
    return bcrypt_context.hash(password)


def verify_password(hash_password, plain_password):
    """
    Vérifie que le mot de passe non cryté correspond au mote de passe crypté
    :param hash_password:
    :param plain_password:
    :return: booleen
    """
    return bcrypt_context.verify(hash_password, plain_password)


def authenticate_user(username: str, password: str, db):
    """
    Fonction d'authentification.
    recherche dans la base de donnée une entrée correspondant au nom d'user
    donné en param.
    Si aucun nom ou si le password ne correspond pas avec celui encrypté on
    retourne False, sinon on retourne l'user
    :param username:
    :param password:
    :param db:
    :return: user si True, else False
    """
    user = db.query(User).filter(User.username == username). \
        first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(username: str, user_id: int, expires_delta: Optional[timedelta] = None):
    encode = {"sub": username, "id": user_id}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    encode.update({"exp": expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGO)


async def get_current_user(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGO])
        username: str = payload.get("sub")
        id_user: int = payload.get("id")
        if username is None or id_user is None:
            raise get_user_exception()
        return {"username": username, "id": id_user}
    except JWTError:
        raise get_user_exception()


@router.post("/create/user")
async def create_new_user(create_user: CreateUser, db: Session = Depends(get_db)):
    create_user_model = User()
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


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise token_exception()
    token_expires = timedelta(minutes=20)
    token = create_access_token(user.username,
                                user.id_user,
                                expires_delta=token_expires)
    return {"token": token}


def get_user_exception():
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    return credentials_exception


def token_exception():
    token_exception_response = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"}
    )
    return token_exception_response
