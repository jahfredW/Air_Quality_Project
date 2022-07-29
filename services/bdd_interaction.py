import api_create_models
from api_connect import engine
from fastapi import FastAPI
from routers import auth, pollution, villes


app = FastAPI()

#api_create_models.Base.metadata.drop_all(bind=engine)
api_create_models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(pollution.router)
app.include_router(villes.router)





