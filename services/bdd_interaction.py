import sys
sys.path.append("..")

import api_create_models
from api_connect import engine
from fastapi import FastAPI, Depends
from routers import auth, pollution, villes, departements
from compagny import compagnyapis, dependencies

app = FastAPI()

#api_create_models.Base.metadata.drop_all(bind=engine)
api_create_models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(pollution.router)
app.include_router(villes.router)
app.include_router(departements.router)
app.include_router(
    compagnyapis.router,
    prefix="/companyapis",
    tags=["companyapis"],
    dependencies=[Depends(dependencies.get_token_header)],
    responses={418: {"description": "Internal Use Only"}}
)





