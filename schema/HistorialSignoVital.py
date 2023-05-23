from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class historialSignoVitalBase(BaseModel):
    fecha: datetime
    valor: float
    signo_id:int
    paciente_id: int

class historialSignoVitalSchema(historialSignoVitalBase):
    id:int

    class Config:
        orm_mode = True