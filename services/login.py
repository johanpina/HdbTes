from fastapi import APIRouter, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from utils.db import DataBaseConnection, run_query
from schema.Usuario import Usuario
import jwt

security = HTTPBasic()
login = APIRouter()


def crear_token(Usuario):
    logeado = {"cedula": Usuario['cedula']}
    token = jwt.encode(logeado, Usuario['password'], algorithm="HS256")
    return token



@login.get("/")
def logeo(cedula, password):
    cur= run_query("SELECT * FROM Usuario WHERE Cedula = %(valor)s", {"valor":cedula})
    for data in cur:
        user = data
    if not user or not user['password'] == password:
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos, verificar datos")
    else:
        token = crear_token(user)

    return {"Acess token": token}