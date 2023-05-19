from pydantic import BaseModel

class PersonalMedicoBase(BaseModel):
    usuario_id:int
    tarjetaProfesional: str
    especialidad: str
    tipo_personal: str

class PersonalMedicoSchema(PersonalMedicoBase):
    id: int

    class Config:
        orm_mode: True
    
