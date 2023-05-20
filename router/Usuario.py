import sys
sys.path.append("..")
import psycopg2

from fastapi import APIRouter, HTTPException
from schema.Usuario import UsuarioSchema
from utils.dbAlchemy import session
from models.model import UsuarioModel
from schema.Usuario import UsuarioSchema,UsuarioBase
from typing import List

user = APIRouter()

@user.get("/all/", response_model=List[UsuarioSchema])
async def get_allUsers():
    usuarios = session.query(UsuarioModel).all()
    return usuarios

@user.post("/", response_model=UsuarioSchema)
async def create_usuario(usuario: UsuarioBase):
    db_usuario = UsuarioModel(**usuario.dict())
    session.add(db_usuario)
    session.commit()
    session.refresh(db_usuario)
    return db_usuario

@user.put("/", response_model=UsuarioSchema)
async def update_usuario(usuario: UsuarioSchema):
    usuarioac = session.query(UsuarioModel).filter_by(id = usuario.id).one()

    if usuarioac:

        usuarioac.nombre = usuario.nombre
        usuarioac.apellido = usuario.apellido
        usuarioac.cedula = usuario.cedula
        usuarioac.edad = usuario.edad
        usuarioac.telefono = usuario.telefono
        usuarioac.email = usuario.email
        usuarioac.password = usuario.password
        usuarioac.direccion = usuario.direccion

        session.commit()
        print("Registro Actualizado exitosamente")
    
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuarioac
    

@user.delete("/")
def delete_usuario(idregistro: int):
    usuario = session.query(UsuarioModel).filter(UsuarioModel.id == idregistro).one()

    if usuario:
        session.delete(usuario)
        session.commit()
        print("Registro eliminado exitosamente")
        return {"mensaje": "Usuario Eliminado"}
    else:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")


    
