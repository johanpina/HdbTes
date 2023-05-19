from pydantic import BaseModel

class SignosVitalesBase(BaseModel):
    nombre_signo: str
    unidad: str

class SignosVitalesSchema(SignosVitalesBase):
    id:int

    class Config:
        orm_mode: True