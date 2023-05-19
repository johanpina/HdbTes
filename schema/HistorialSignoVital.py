from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class historialSignoVitalSchema(BaseModel):
    id:Optional[int]
    fecha: datetime
    valor: float
    signo_id:int
    paciente_id: int