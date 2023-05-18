from sqlalchemy import Table, Column, Integer, String,DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models.Paciente import PacienteModel
from models.PersonalMedico import PersonalMedicoModel
#from utils.dbAlchemy import meta, engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class historialCuidadosModel(Base):
    __tablename__ = 'historialcuidados'
    id = Column(Integer, primary_key=True)
    fecha_inicial = Column(DateTime)
    fecha_final = Column(DateTime)
    cuidado = Column(String)
    medico_id = Column(Integer, ForeignKey(PersonalMedicoModel.id))
    paciente_id = Column(Integer, ForeignKey(PacienteModel.id))
    descripcion = Column(String)
    




"""
historialCuidados = Table("historialcuidados", meta, Column("id", Integer, primary_key=True), Column("fecha_inicial",DateTime), Column("fecha_final",DateTime), 
                          Column("cuidado", String(255)), Column("medico_id", Integer, ForeignKey("personalmedico.id")), 
                          Column("paciente_id",Integer, ForeignKey("paciente.id")), Column("descripcion", String(255)))

    Column("",)
"""