import jsons
import sys



sys.path.append("..")

from fastapi import FastAPI, Form, HTTPException
import traceback as tb
from pollution_api import PollutionAPI
from fastapi.middleware.cors import CORSMiddleware
from business.components.pollution import Pollution
from custom_exept.application_exception import ApplicationException
from starlette.responses import HTMLResponse, JSONResponse

from presentation.web.controllers.error_controller import ErrorController
from services.routers import pollution


serveur = FastAPI()

origins = ["*"]

serveur.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

serveur.include_router(pollution.router)


@serveur.get("/")
async def root():
    return {"message": 'API de l\'application \"on va courir\" !'}


@serveur.get("/environnement")
async def read_environment():
    try:
        api = PollutionAPI()
        return api.get_environment()

    except ApplicationException as ae:
        print("Erreur : " + str(ae))
        raise HTTPException(status_code=520, detail=str(ae))
    except Exception as e:
        print("erreur :" + str(e))
        raise HTTPException(status_code=500, detail="Internal serveur error")


@serveur.post("/previsions")
async def get_prev(ville: str = Form(...)):
    try:
        api = PollutionAPI()
        prev = jsons.dump(api.get_previsions(ville))
        return prev
    except ApplicationException as ae:
        print("Erreur: " + str(ae))
        raise HTTPException(status_code=520, detail=str(ae))
    except Exception as e:
        print("Erreur: " + str(e))
        raise HTTPException(status_code=500, detail="Internal serveur error")


@serveur.post("/previsionsJour")
async def get_prev(ville: str = Form(...)):
    try:
        api = PollutionAPI()
        prev = jsons.dump(api.get_previsions_jour(ville))
        return prev
    except ApplicationException as ae:
        print("Erreur: " + str(ae))
        raise HTTPException(status_code=520, detail=str(ae))
    except Exception as e:
        print("Erreur: " + str(e))
        raise HTTPException(status_code=500, detail="Internal serveur error")


