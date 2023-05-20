import sys
sys.path.append("..")

from fastapi import APIRouter, HTTPException
from utils.dbAlchemy import session
from models.model import signosVitalesModel
from schema.SignosVitales import SignosVitalesSchema, SignosVitalesBase
from typing import List



signosVitales = APIRouter()

@signosVitales.get("/all/", response_model=List[SignosVitalesSchema])
def get_signosVitales():
    Signos = session.query(signosVitalesModel).all()
    return Signos

@signosVitales.post("/", response_model=SignosVitalesSchema)
def create_signosVitales(signosVitales: SignosVitalesBase):
    db_signo = signosVitalesModel(**signosVitales.dict())
    session.add(db_signo)
    session.commit()
    session.refresh(db_signo)
    return db_signo

@signosVitales.put("/", response_model=SignosVitalesSchema)
def update_signosVitales(signosVitales: SignosVitalesSchema):
    signovital = session.query(signosVitalesModel).filter_by(id = signosVitales.id).one()

    if signovital:

        signovital.nombre_signo = signosVitales.nombre_signo
        signovital.unidad = signosVitales.unidad
        session.commit()
        print("Registro Actualizado exitosamente")
    
    else:
        raise HTTPException(status_code=404, detail="Signo Vital no encontrado")
    
    return signovital

@signosVitales.delete("/")
def delete_signoVital(idregistro: int):
    signovital = session.query(signosVitalesModel).filter(signosVitalesModel.id == idregistro).one()

    if signovital:
        session.delete(signovital)
        session.commit()
        print("Registro eliminado exitosamente")
        return {"mensaje": "Signo Vital Eliminado"}
    else:
        raise HTTPException(status_code=404, detail="Signo Vital no encontrado")
