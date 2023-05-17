import sys
sys.path.append("..")
import psycopg2

from fastapi import APIRouter, HTTPException
from utils.db import DataBaseConnection, run_query
#from utils.dbAlchemy import conn

#--------
from utils.dbAlchemy import session
from models.HistorialCuidados import historialCuidadosModel
from schema.HistorialCuidados import HistorialCuidados
from sqlalchemy import func, select


historialCuidados = APIRouter()
#cur = conn.cursor()

@historialCuidados.get("/all/")
def get_historialCuidados():
    historiales = session.query(historialCuidadosModel).all()
    return historiales

@historialCuidados.post("/")
def create_historial_cuidados(historialCuidados: HistorialCuidados):
    new_historial_Cuidado = historialCuidadosModel(fecha_inicial=historialCuidados.fecha_inicial, 
                                                     fecha_final=historialCuidados.fecha_final,
                                                     cuidado=historialCuidados.cuidado,
                                                     medico_id=historialCuidados.medico_id,
                                                     paciente_id=historialCuidados.paciente_id,
                                                     descripcion=historialCuidados.cuidado)
    result = session.add(new_historial_Cuidado)
    session.commit()
    return result


@historialCuidados.put("/")
def update_historial_Cuidados(historialCuidados: HistorialCuidados):
    historialCuidado = session.query(historialCuidadosModel).filter_by(id = historialCuidados.id).first()

    if historialCuidado:
        historialCuidado.fecha_inicial = historialCuidados.fecha_inicial
        historialCuidado.fecha_final = historialCuidados.fecha_final
        historialCuidado.cuidado = historialCuidados.cuidado
        historialCuidado.medico_id = historialCuidados.medico_id
        historialCuidado.paciente_id = historialCuidados.paciente_id
        historialCuidado.descripcion = historialCuidados.descripcion
        session.commit()
        print("Registro Actualizado exitosamente")
    
    else:
        print("No se encontro el registro con el ID proporcionado")

@historialCuidados.delete("/")
def delete_historial_cuidado(idregistro: int):
    historialCuidado = session.query(historialCuidadosModel).filter_by(id = idregistro).first()

    if historialCuidado:
        session.delete(historialCuidado)
        session.commit()
        print("Registro eliminado exitosamente")
    
    else:
        print("No se encontro el registro con el ID proporcionado")

# conn.execute(historialCuidados.select()).fetchall()