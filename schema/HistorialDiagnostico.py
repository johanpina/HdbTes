from pydantic import BaseModel
from datetime import datetime

class HistorialDiagnosticoBase(BaseModel):
    medico_id:int
    fecha:datetime
    paciente_id:int
    diagnostico_id:int

class HistorialDiagnosticoSchema(HistorialDiagnosticoBase):
    id:int

    class Config:
        orm_mode: True