import sys
sys.path.append("..")

import api_create_models
import traceback as tb
from api_connect import engine
from fastapi import FastAPI, Depends, Form, APIRouter
from fastapi.responses import HTMLResponse
from routers import auth, pollution, villes, departements
from compagny import compagnyapis, dependencies
from fastapi.staticfiles import StaticFiles
from presentation.web.controllers.error_controller import ErrorController
from presentation.web.controllers.index_controller import IndexController
from presentation.web.controllers.pollution_ville_bulma_controller import PollutionVilleBulmaController
from utils.configuration import Configuration



#api_create_models.Base.metadata.drop_all(bind=engine)
api_create_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/images", StaticFiles(directory=Configuration().get_instance().web_local_images_directory), name="images")
app.mount("/css", StaticFiles(directory=Configuration().get_instance().web_local_css_directory), name="css")
app.mount("/scripts", StaticFiles(directory=Configuration().get_instance().web_local_scripts_directory), name="scripts")


router = APIRouter(
    prefix="/pollution",
    tags=["pollution"],
    responses={404: {"description": "Not found"}}
)

app.include_router(pollution.router)

"""
app.include_router(auth.router)

app.include_router(villes.router)
app.include_router(departements.router)
app.include_router(
    compagnyapis.router,
    prefix="/companyapis",
    tags=["companyapis"],
    dependencies=[Depends(dependencies.get_token_header)],
    responses={418: {"description": "Internal Use Only"}}
)
"""

@app.get("/")
async def root():
    try:
        controller = IndexController()
        return HTMLResponse(content=controller.index(), status_code=200)
    except Exception as error:
        controller = ErrorController()
        errorMessage = ''.join(tb.format_exception(None, error, error.__traceback__))
        errorMessage = errorMessage.replace(",", "\n")
        htmlMessage = controller.error(errorMessage)
        return HTMLResponse(content=htmlMessage, status_code=500)

"""
@app.post("/villes")
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