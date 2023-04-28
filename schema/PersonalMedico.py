from pydantic import BaseModel

class PersonalMedico(BaseModel):
    id: int
    usuario_id:int
    tarjetaProfesional: str
    especialidad: str
    tipo_personal: str
    
