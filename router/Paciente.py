import sys
sys.path.append("..")
import psycopg2
from fastapi import APIRouter
from utils.dbAlchemy import session
from models.model import PacienteModel
from utils.dbAlchemy import session
from typing import List
from schema.Paciente import PacienteSchema
from models.model import PacienteModel, UsuarioModel, FamiliarDesignadoModel
from schema.Usuario import UsuarioSchema

paciente = APIRouter()

@paciente.get("/all/", response_model=List[PacienteSchema])
async def listar_pacientes():
    pacientes = session.query(PacienteModel).all()
    return pacientes

@paciente.get("/pacientesporfamiliar", response_model=List[UsuarioSchema])
def listar_pacientesporfamiliar(idfamiliar: int):
    PacientesAcargo = session.query(FamiliarDesignadoModel, PacienteModel, UsuarioModel).join(PacienteModel, FamiliarDesignadoModel.id== PacienteModel.familiar_id).join(UsuarioModel, PacienteModel.usuario_id == UsuarioModel.id).filter(FamiliarDesignadoModel.usuario_id == idfamiliar).all()
    resultado_json = []
    for item in PacientesAcargo:
        tabla_data = item[2].__dict__
        resultado_json.append({
            key: value for key, value in tabla_data.items() if not key.startswith('_')
        })
    return resultado_json   

