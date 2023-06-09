from fastapi import APIRouter, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from utils.db import DataBaseConnection, run_query
from schema.Usuario import UsuarioSchema
from models.model import UsuarioModel, PersonalMedicoModel, FamiliarDesignadoModel, PacienteModel
from utils.dbAlchemy import session
import jwt


security = HTTPBasic()
login = APIRouter()


def crear_token(usuario: UsuarioSchema):
    logeado = {"cedula": usuario.cedula}
    token = jwt.encode(logeado, usuario.password, algorithm="HS256")
    return usuario, token



@login.get("/")
def logeo(cedulausuario, passwordusuario):
    usuarioac = session.query(UsuarioModel).filter_by(cedula = cedulausuario).first()
    rol=[]
    if usuarioac and usuarioac.password == passwordusuario:
        token = crear_token(usuarioac)
    else: 
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos, verificar datos")
    
    print(usuarioac.id)
    doctor = usuarioac.personalmedico
    familiar = usuarioac.familiardesignado
    paciente = usuarioac.paciente
    
    if doctor:
        rol.append("doctor")

    if familiar:
        rol.append("familiar")

    if paciente:
        rol.append("paciente")

    return {"auth": token, "rol":rol  }