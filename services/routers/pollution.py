import json
import sys

from business.components.pollution import Pollution

sys.path.append("..")

import traceback as tb
import api_create_models
import geopy
from api_connect import engine, SessionLocal
from fastapi import FastAPI, Depends, HTTPException, APIRouter, Form
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from presentation.web.controllers.error_controller import ErrorController
from presentation.web.controllers.index_controller import IndexController
from presentation.web.controllers.pollution_ville_controller import PollutionVilleController
from presentation.web.controllers.pollution_ville_bulma_controller import PollutionVilleBulmaController
from utils.configuration import Configuration
import requests



router = APIRouter(
    prefix="/pollution",
    tags=["pollution"],
    responses={404: {"description": "Not found"}}
)



#api_create_models.Base.metadata.drop_all(bind=engine)
api_create_models.Base.metadata.create_all(bind=engine)





def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


"""
@router.get('/all')
async def read_all(db: Session = Depends(get_db)):
     pollution_model = db.query(api_create_models.Pollution).all()
     if pollution_model is not None:
         print(pollution_model)
         return pollution_model
     else:
        raise HTTPException(status_code=404, detail='Not Found')
"""

@router.post("/villes")
async def read_pollution_ville(ville: str = Form(...)):
    try:
        controller = PollutionVilleBulmaController()
        return HTMLResponse(content=controller.read_pollution_ville(ville), status_code=200)

    except Exception as error:
        controller = ErrorController()
        errorMessage = ''.join(tb.format_exception(None, error, error.__traceback__))
        errorMessage = errorMessage.replace(",", "\n")
        htmlMessage = controller.error(errorMessage)
        return HTMLResponse(content=htmlMessage, status_code=500)

@router.get("/{villes}/aqi")
async def read_pollution_ville(villes):

    try:
        pollution = Pollution(villes)
        response = {
            "villes": villes,
            "indice": pollution.get_aqi()[0]
        }
        return response

    except Exception as error:
        controller = ErrorController()
        errorMessage = ''.join(tb.format_exception(None, error, error.__traceback__))
        errorMessage = errorMessage.replace(",", "\n")
        htmlMessage = controller.error(errorMessage)
        return HTMLResponse(content=htmlMessage, status_code=500)

@router.get("/{villes}/")
async def read_pollution_ville(villes):

    try:
        pollution = Pollution(villes)
        response = {"datas": {
            "villes": villes,
            "datas": pollution.get_pollution_ville()
        }}
        return response

    except Exception as error:
        controller = ErrorController()
        errorMessage = ''.join(tb.format_exception(None, error, error.__traceback__))
        errorMessage = errorMessage.replace(",", "\n")
        htmlMessage = controller.error(errorMessage)
        return HTMLResponse(content=htmlMessage, status_code=500)











