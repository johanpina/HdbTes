from pydantic import BaseModel
from datetime import datetime

class HistorialCuidados(BaseModel):
    id:int
    fecha_inicial: datetime
    fecha_final: datetime
    cuidado: str
    medico_id: int
    paciente_id: int
    descripcion: str
