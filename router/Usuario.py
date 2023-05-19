import sys
sys.path.append("..")
import psycopg2

from fastapi import APIRouter, HTTPException
from schema.Usuario import UsuarioSchema
from utils.dbAlchemy import session
from models.Usuario import UsuarioModel

user = APIRouter()


@user.get("/all/")
def get_allUsers():
    Usuarios = session.query(UsuarioModel).all()
    return Usuarios

@user.post("/")
def create_usuario(usuario: UsuarioSchema):
    new_usuario = UsuarioModel(id=usuario.id ,nombre= usuario.nombre, apellido= usuario.apellido, cedula = usuario.cedula, edad= usuario.edad, telefono = usuario.telefono, email= usuario.email, password= usuario.password, direccion = usuario.direccion)
    result = session.add(new_usuario)
    session.commit()
    return result

@user.put("/")
def update_usuario(usuario: UsuarioSchema):
    usuarioac = session.query(UsuarioModel).filter_by(id = usuario.id).first()

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
        print("No se encontro el registro con el ID proporcionado.")
    print(usuarioac.nombre)
    return usuarioac
    

@user.delete("/")
def delete_usuario(idregistro: int):
    usuario = session.query(UsuarioModel).filter_by(id = idregistro).first()

    if usuario:
        session.delete(usuario)
        session.commit()
        print("Registro eliminado exitosamente")
    
    else:
        print("No se encontro el registro con el ID proporcionado")
