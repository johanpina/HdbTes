from sqlalchemy import Table, Column, Integer, String,DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class signosVitalesModel(Base):
    __tablename__ = 'signosvitales'  #poner cuidado cuando se ponga el nombre de las talbas
    id = Column(Integer, primary_key=True)
    nombre_signo = Column(String)
    unidad = Column(String)




"""
signosVitales = Table("signosvitales", meta, Column("id", Integer, primary_key=True), Column("nombre_signo",String(255)),
                          Column("unidad", String(255)))

    Column("",)
"""