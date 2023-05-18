from fastapi import APIRouter, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from utils.db import DataBaseConnection, run_query
from schema.Usuario import UsuarioSchema
from models.Usuario import UsuarioModel
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

    if usuarioac and usuarioac.password == passwordusuario:
        token = crear_token(usuarioac)
    else: 
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos, verificar datos")

    return {"Acess token": token}