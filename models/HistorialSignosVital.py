from sqlalchemy import Table, Column, Integer, String,DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from models.Paciente import PacienteModel
from models.SignosVitales import signosVitalesModel

Base = declarative_base()

class historialSignosVitalModel(Base):
    __tablename__ = 'historialsignovital'  #poner cuidado cuando se ponga el nombre de las talbas
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    fecha = Column(DateTime)
    valor = Column(Float)
    signo_id = Column(Integer, ForeignKey(signosVitalesModel.id))
    paciente_id = Column(Integer, ForeignKey(PacienteModel.id))




"""
historialSignosVital = Table("historialsignovital", meta, Column("id", Integer, primary_key=True), Column("fecha",DateTime),
                          Column("valor", Float), Column("signo_id", Integer, ForeignKey("signosvitales.id")), 
                          Column("paciente_id",Integer, ForeignKey("paciente.id")))

    Column("",)
"""