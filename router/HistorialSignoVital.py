import sys
sys.path.append("..")

from fastapi import APIRouter, HTTPException
from utils.db import DataBaseConnection, run_query

from utils.dbAlchemy import session
from models.HistorialSignosVital import historialSignosVitalModel
from schema.HistorialSignoVital import historialSignoVitalSchema



historialSignosVital = APIRouter()

@historialSignosVital.get("/all/")
def get_historialSignosVitales():
    historialSignos = session.query(historialSignosVitalModel).all()
    return historialSignos

@historialSignosVital.post("/")
def create_historialSignosVitales(historialSignosVitales: historialSignoVitalSchema):
    new_historialSignoVital = historialSignosVitalModel(id=historialSignosVitales.id ,fecha= historialSignosVitales.fecha, valor= historialSignosVitales.valor, signo_id= historialSignosVitales.signo_id, paciente_id= historialSignosVitales.paciente_id)
    result = session.add(new_historialSignoVital)
    session.commit()
    return result

@historialSignosVital.put("/")
def update_historialSignosVitales(historialSignosVitales: historialSignoVitalSchema):
    historialsignovital = session.query(historialSignosVitalModel).filter_by(id = historialSignosVitales.id).first()

    if historialsignovital:

        historialsignovital.fecha = historialSignosVitales.fecha
        historialsignovital.valor = historialSignosVitales.valor
        historialsignovital.signo_id = historialSignosVitales.signo_id
        historialsignovital.paciente_id = historialSignosVitales.paciente_id
        session.commit()
        print("Registro Actualizado exitosamente")
    
    else:
        print("No se encontro el registro con el ID proporcionado.")

@historialSignosVital.delete("/")
def delete_historialSignoVital(idregistro: int):
    historialsignovital = session.query(historialSignosVitalModel).filter_by(id = idregistro).first()

    if historialsignovital:
        session.delete(historialsignovital)
        session.commit()
        print("Registro eliminado exitosamente")
    
    else:
        print("No se encontro el registro con el ID proporcionado")