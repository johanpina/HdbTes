from pydantic import BaseModel

class FamiliarDesignadoBase(BaseModel):
    id:int
    usuario_id:int
    telefono_alterno:str

class FamiliarDesignadoSchema(FamiliarDesignadoBase):
    id: int

    class Config:
        orm_mode = True