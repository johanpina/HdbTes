from sqlalchemy import create_engine, MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:2303@localhost:5432/HospitalizacionenCasa')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()