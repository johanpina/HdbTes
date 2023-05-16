from pydantic import BaseModel
from datetime import datetime

class HistorialSignoVital(BaseModel):
    id:int
    fecha: datetime
    valor: float
    signo_id:int
    paciente_id: int