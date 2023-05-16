from pydantic import BaseModel

class SignosVitales(BaseModel):
    id:int
    nombre_signo: str
    unidad: str