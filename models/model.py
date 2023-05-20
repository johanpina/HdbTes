from sqlalchemy import Table, Column, Integer, String,DateTime, ForeignKey, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class historialCuidadosModel(Base):
    __tablename__ = 'historialcuidados'
    id = Column(Integer, primary_key=True)
    fecha_inicial = Column(DateTime)
    fecha_final = Column(DateTime)
    cuidado = Column(String)
    medico_id = Column(Integer, ForeignKey("personalmedico.id"))
    paciente_id = Column(Integer, ForeignKey("paciente.id"))
    descripcion = Column(String)
    
    #foraneo para otras tablas

    #recibo de foraneo de otras tablas

    personalmedico = relationship("PersonalMedicoModel", back_populates="historialcuidados")
    paciente = relationship("PacienteModel", back_populates="historialcuidados")

class PersonalMedicoModel(Base):
    __tablename__ = 'personalmedico'  #poner cuidado cuando se ponga el nombre de las talbas
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    tarjeta_profesional = Column(String)
    especialidad = Column(String)
    tipo_personal = Column(String)

    #foraneo para otras tablas

    personalacargo = relationship("PersonalACargoModel", back_populates="personalmedico")
    historialcuidados = relationship("historialCuidadosModel", back_populates="personalmedico")

    #recibo de foraneo de otras tablas

    usuario = relationship("UsuarioModel", back_populates="personalmedico")

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

    #foraneo para otras tablas

    personalmedico = relationship("PersonalMedicoModel", back_populates="usuario")
    paciente = relationship("PacienteModel", back_populates="usuario")
    familiardesignado = relationship("FamiliarDesignadoModel", back_populates="usuario")

    #recibo de foraneo de otras tablas

class FamiliarDesignadoModel(Base):
    __tablename__ = 'familiardesignado'  #poner cuidado cuando se ponga el nombre de las talbas
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    telefono_alterno = Column(String)

    #foraneo para otras tablas
    paciente = relationship("PacienteModel", back_populates="familiardesignado")

    #recibo de foraneo de otras tablas

    usuario = relationship("UsuarioModel", back_populates="familiardesignado")

class historialSignosVitalModel(Base):
    __tablename__ = 'historialsignovital'  #poner cuidado cuando se ponga el nombre de las talbas
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    fecha = Column(DateTime)
    valor = Column(Float)
    signo_id = Column(Integer, ForeignKey("signosvitales.id"))
    paciente_id = Column(Integer, ForeignKey("paciente.id"))

    #foraneo para otras tablas

    #recibo de foraneo de otras tablas

    signosvitales = relationship("signosVitalesModel", back_populates="historialsignovital")
    paciente = relationship("PacienteModel", back_populates="historialsignovital")
    
class PacienteModel(Base):
    __tablename__ = 'paciente'  #poner cuidado cuando se ponga el nombre de las talbas
    id = Column(Integer, primary_key=True)
    familiar_id = Column(Integer, ForeignKey("familiardesignado.id"))
    usuario_id = Column(Integer, ForeignKey("usuario.id"))

    #foraneo para otras tablas

    personalacargo = relationship("PersonalACargoModel", back_populates="paciente")
    historialcuidados = relationship("historialCuidadosModel", back_populates="paciente")
    historialsignovital = relationship("historialSignosVitalModel", back_populates="paciente")

    #recibo de foraneo de otras tablas

    usuario = relationship("UsuarioModel", back_populates="paciente")
    familiardesignado = relationship("FamiliarDesignadoModel", back_populates="paciente")

class PersonalACargoModel(Base):
    __tablename__ = 'personalacargo'  #poner cuidado cuando se ponga el nombre de las talbas
    id = Column(Integer, primary_key=True)
    medico_id = Column(Integer, ForeignKey("personalmedico.id"))
    paciente_id = Column(Integer, ForeignKey("paciente.id"))
    paciente_activo = Column(Boolean)

    #foraneo para otras tablas



    #recibo de foraneo de otras tablas

    personalmedico = relationship("PersonalMedicoModel", back_populates="personalacargo")
    paciente = relationship("PacienteModel", back_populates="personalacargo")


class signosVitalesModel(Base):
    __tablename__ = 'signosvitales'  #poner cuidado cuando se ponga el nombre de las talbas
    id = Column(Integer, primary_key=True)
    nombre_signo = Column(String)
    unidad = Column(String)

    #foraneo para otras tablas

    historialsignovital = relationship("historialSignosVitalModel", back_populates="signosvitales")

    #recibo de foraneo de otras tablas


class notificacionesModel():
    destino: str
    asunto: str
    mensaje: str