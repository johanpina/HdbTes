from fastapi import APIRouter, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from utils.db import DataBaseConnection, run_query
from schema.Usuario import UsuarioSchema
from models.Usuario import UsuarioModel
from utils.dbAlchemy import session
import jwt
from models.PersonalMedico import PersonalMedicoModel
from models.FamiliarDesignado import FamiliarDesignadoModel
from models.Paciente import PacienteModel

security = HTTPBasic()
login = APIRouter()


def crear_token(usuario: UsuarioSchema):
    logeado = {"cedula": usuario.cedula}
    token = jwt.encode(logeado, usuario.password, algorithm="HS256")
    return usuario, token



@login.get("/")
def logeo(cedulausuario, passwordusuario):
    usuarioac = session.query(UsuarioModel).filter_by(cedula = cedulausuario).first()
    id = usuarioac.id
    rol=[]
    if usuarioac and usuarioac.password == passwordusuario:
        token = crear_token(usuarioac)
    else: 
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos, verificar datos")
    
    print(usuarioac.id)
    doctor = session.query(PersonalMedicoModel).filter(PersonalMedicoModel.usuario_id == id).first()
    familiar = session.query(FamiliarDesignadoModel).filter(FamiliarDesignadoModel.usuario_id == id).first()
    paciente = session.query(PacienteModel).filter(PacienteModel.usuario_id == id).first()


    if doctor:
        rol.append("medico")
    if familiar:
        rol.append("familiar")
    if paciente:
        rol.append("paciente")

    return {"auth": token, "rol":rol}