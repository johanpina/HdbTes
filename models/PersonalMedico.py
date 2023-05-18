from sqlalchemy import Table, Column, Integer, String,DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.Usuario import UsuarioModel


Base = declarative_base()

class PersonalMedicoModel(Base):
    __tablename__ = 'personalmedico'  #poner cuidado cuando se ponga el nombre de las talbas
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey(UsuarioModel.id))
    tarjeta_profesional = Column(String)
    especialidad = Column(String)
    tipo_personal = Column(String)
