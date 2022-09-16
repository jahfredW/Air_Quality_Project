import sys

sys.path.append("..")

from fastapi import FastAPI
from pollution_api import PollutionAPI
from fastapi.middleware.cors import CORSMiddleware

serveur = FastAPI()

origins = ["*"]

serveur.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@serveur.get("/")
async def root():
    return {"message": 'API de l\'application \"on va courir\" !'}

@serveur.get("/environnement")
async def read_environment():
    api = PollutionAPI()
    return api.get_environment()
