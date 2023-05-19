from pydantic import BaseModel

class PacienteBase(BaseModel):
    familiar_id:int
    usuario_id:int

class PacienteSchema(PacienteBase):
    id: int

    class Config:
        orm_mode: True