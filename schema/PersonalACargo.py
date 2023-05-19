from pydantic import BaseModel

class PersonalACargoSchema(BaseModel):
    id: int
    medico_id:int
    paciente_id: int
    paciente_activo: bool
    