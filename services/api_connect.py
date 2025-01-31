from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://dev:Farte512!@localhost/test2"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'connect_timeout' : 10})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
