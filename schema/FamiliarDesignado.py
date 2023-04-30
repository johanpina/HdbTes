from pydantic import BaseModel

class FamiliarDesignado(BaseModel):
    id:int
    usuario_id:int
    telefono_alterno:str