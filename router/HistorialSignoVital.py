import sys
sys.path.append("..")

from fastapi import APIRouter, HTTPException
from utils.db import DataBaseConnection, run_query

from utils.dbAlchemy import session
from models.model import historialSignosVitalModel
from schema.HistorialSignoVital import historialSignoVitalSchema, historialSignoVitalBase
from typing import List



historialSignosVital = APIRouter()

@historialSignosVital.get("/all/", response_model=List[historialSignoVitalSchema])
def get_historialSignosVitales():
    historialSignos = session.query(historialSignosVitalModel).all()
    return historialSignos

@historialSignosVital.post("/", response_model=historialSignoVitalSchema)
def create_historialSignosVitales(historialSignosVitales: historialSignoVitalBase):
    db_historialSignoVital = historialSignosVitalModel(**historialSignosVitales.dict())
    session.add(db_historialSignoVital)
    session.commit()
    session.refresh(db_historialSignoVital)
    return db_historialSignoVital

@historialSignosVital.put("/", response_model=historialSignoVitalSchema)
def update_historialSignosVitales(historialSignosVitales: historialSignoVitalSchema):
    historialsignovital = session.query(historialSignosVitalModel).filter_by(id = historialSignosVitales.id).one()

    if historialsignovital:

        historialsignovital.fecha = historialSignosVitales.fecha
        historialsignovital.valor = historialSignosVitales.valor
        historialsignovital.signo_id = historialSignosVitales.signo_id
        historialsignovital.paciente_id = historialSignosVitales.paciente_id
        session.commit()
        print("Registro Actualizado exitosamente")
    
    else:
        raise HTTPException(status_code=404, detail="historial de signo vital no encontrado")
    
    return historialsignovital


@historialSignosVital.delete("/")
def delete_historialSignoVital(idregistro: int):
    historialsignovital = session.query(historialSignosVitalModel).filter(historialSignosVitalModel.id == idregistro).first()

    if historialsignovital:
        session.delete(historialsignovital)
        session.commit()
        return {"mensaje": "historial signo vital Eliminado"}
    
    else:
        raise HTTPException(status_code=404, detail="historial signo vital no encontrado")
