from sqlalchemy import Table, Column, Integer, String,DateTime, ForeignKey, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.Paciente import PacienteModel
from models.PersonalMedico import PersonalMedicoModel


Base = declarative_base()

class PersonalACargoModel(Base):
    __tablename__ = 'personalacargo'  #poner cuidado cuando se ponga el nombre de las talbas
    id = Column(Integer, primary_key=True)
    medico_id = Column(Integer, ForeignKey(PersonalMedicoModel.id))
    paciente_id = Column(Integer, ForeignKey(PacienteModel.id))
    paciente_activo = Column(Boolean)
