from fastapi import FastAPI, Depends, HTTPException
import api_create_models
from api_connect import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

api_create_models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get('/{code_postal}')
async def read_database(code_postal: int, db: Session = Depends(get_db)):
     pollution_model = db.query(api_create_models.Pollution).filter(api_create_models.Pollution.id_ville == code_postal)\
         .first()
     if pollution_model is not None:
         return pollution_model
     raise HTTPException(status_code=404, detail='Not Found')

