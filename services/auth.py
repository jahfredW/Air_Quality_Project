from fastapi import FastAPI
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import jwt
from pydantic import BaseModel
from typing import Optional
from passlib.context import CryptContext
from api_create_models import User

SECRET_KEY = "oizejdoùzed9+4z5e+d9zedjzoih"
ALGO = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated='auto')

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")


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
    user = db.query(User).filter(User.username == username).\
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
    encode.update({"exp" : expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGO)



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

