from pydantic import BaseModel

class Usuario(BaseModel):
    id:int
    nombre: str
    apellido: str
    cedula:str
    edad: int
    telefono: str
    email: str
    password:str
    direccion:str