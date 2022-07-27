from sqlalchemy import Boolean, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from api_connect import Base


class Departement(Base):
    __tablename__ = 'departement'
    id_departement = Column(Integer, primary_key= True, index= True)
    nom = Column(String)
    code = Column(String)
    ville_child = relationship('Ville', back_populates="departement")


class Ville(Base):
    __tablename__ = 'ville'
    id_ville = Column(Integer, primary_key= True, index= True)
    nom = Column(String)
    code_postal = Column(Integer)
    id_departement = Column(Integer, ForeignKey('departement.id_departement'))
    pollution_child = relationship('Pollution', back_populates="ville")
    departement = relationship('Departement', back_populates="ville_child")


class Pollution(Base):
    __tablename__ = "pollution"
    id_pollution = Column(Integer, primary_key= True, index= True )
    aqi = Column(Integer)
    co = Column(Float)
    no = Column(Float)
    no2 = Column(Float)
    o3 = Column(Float)
    so2 = Column(Float)
    pm2_5 = Column(Float)
    pm10 = Column(Float)
    nh3 = Column(Float)
    day = Column(Date)
    last_update = Column(Date)
    id_ville = Column(Integer, ForeignKey('ville.id_ville'))
    ville = relationship("Ville", back_populates= "pollution_child")


