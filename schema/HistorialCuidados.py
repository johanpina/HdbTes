from pydantic import BaseModel
from datetime import datetime

class HistorialCuidadosBase(BaseModel):
    fecha_inicial: datetime
    fecha_final: datetime
    cuidado: str
    medico_id: int
    paciente_id: int
    descripcion: str

class HistorialCuidadosSchema(HistorialCuidadosBase):
    id:int
    
    class Config:
        orm_mode = True