from pydantic import BaseModel

class Paciente(BaseModel):
    id: int
    familiar_id:int
    usuario_id:int