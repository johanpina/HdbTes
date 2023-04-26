from pydantic import BaseModel

class Usuario(BaseModel):
    id:int
    nombre: str
    apellido: str
    cedula:int
    edad: int
    telefono: str
    email: str
    password:str