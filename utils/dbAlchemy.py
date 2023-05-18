from sqlalchemy import create_engine, MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:123@localhost:5432/HospitalizacionenCasa')
Session = sessionmaker(bind=engine)
session = Session()

'''
engine = create_engine('postgresql://postgres:1234@localhost:5432/HospitalizacionenCasa')
meta = MetaData()
conn = engine.connect()
'''