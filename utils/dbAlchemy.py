from sqlalchemy import create_engine, MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .db import connection_string, parse_connection_string

params = parse_connection_string(connection_string) 
print(params)
# Construir la cadena de conexión para create_engine
engine_str = f"postgresql://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['dbname']}"
engine = create_engine(engine_str)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()