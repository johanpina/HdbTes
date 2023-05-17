from sqlalchemy import Table, Column, Integer, String,DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class UsuarioModel(Base):
    __tablename__ = 'usuario'  #poner cuidado cuando se ponga el nombre de las talbas
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    cedula = Column(String)
    edad = Column(Integer)
    telefono = Column(String)
    email = Column(String)
    password = Column(String)
    direccion = Column(String)