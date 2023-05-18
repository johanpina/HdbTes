from sqlalchemy import Table, Column, Integer, String,DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from models.Usuario import UsuarioModel
from sqlalchemy.orm import relationship


Base = declarative_base()

class FamiliarDesignadoModel(Base):
    __tablename__ = 'familiardesignado'  #poner cuidado cuando se ponga el nombre de las talbas
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey(UsuarioModel.id))
    telefono_alterno = Column(String)