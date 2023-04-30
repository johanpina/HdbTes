from pydantic import BaseModel

class HistorialDiagnostico(BaseModel):
    id:int
    medico_id:int
    fecha:datetime
    paciente_id:int
    diagnostico_id:int