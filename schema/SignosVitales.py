from pydantic import BaseModel

class SignosVitalesSchema(BaseModel):
    id:int
    nombre_signo: str
    unidad: str