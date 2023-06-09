from sqlalchemy import create_engine, MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://uctdfmdutd:C2V1D7334156E6WA$@backendhospitalizacionencasa-server.postgres.database.azure.com:5432/backendhospitalizacionencasa-database')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()