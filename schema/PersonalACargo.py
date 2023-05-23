from pydantic import BaseModel

class PersonalACargoBase(BaseModel):
    medico_id:int
    paciente_id: int
    paciente_activo: bool

class PersonalACargoSchema(PersonalACargoBase):
    id: int

    class Config:
        orm_mode = True
    