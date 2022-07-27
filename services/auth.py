from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated='auto')

def get_hash_password(password):
    return bcrypt_context.hash(password)


class CreateUser(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str

