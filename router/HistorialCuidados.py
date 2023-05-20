import sys
sys.path.append("..")
from fastapi import APIRouter, HTTPException
from utils.db import DataBaseConnection, run_query
#from utils.dbAlchemy import conn

#--------
from utils.dbAlchemy import session
from models.model import historialCuidadosModel,PacienteModel,UsuarioModel, notificacionesModel, FamiliarDesignadoModel
from schema.HistorialCuidados import HistorialCuidadosSchema, HistorialCuidadosBase
from sqlalchemy import func, select
from services import notificaciones
import threading 
from typing import List


historialCuidados = APIRouter()
#cur = conn.cursor()

@historialCuidados.get("/all/", response_model=List[HistorialCuidadosSchema])
def get_historialCuidados():
    historiales = session.query(historialCuidadosModel).all()
    return historiales


@historialCuidados.post("/", response_model=HistorialCuidadosSchema)
def create_historial_cuidados(historialCuidados: HistorialCuidadosBase):
    db_historial_Cuidado = historialCuidadosModel(**historialCuidados.dict())
    session.add(db_historial_Cuidado)
    session.commit()
    session.refresh(db_historial_Cuidado)
    return db_historial_Cuidado

@historialCuidados.get("/send_email/")
def send_email(id:int):
    hilos = []

    historial_cuidado = session.query(historialCuidadosModel).filter(historialCuidadosModel.id == id).first()
    paciente = session.query(PacienteModel).filter(PacienteModel.id == historial_cuidado.paciente_id).first()
    familiarDesignado = session.query(FamiliarDesignadoModel).filter(FamiliarDesignadoModel.id == paciente.familiar_id).first()
    usuario = session.query(UsuarioModel).filter(UsuarioModel.id == familiarDesignado.usuario_id).first()

    notificacionesModel.destino = usuario.email
    notificacionesModel.asunto = historial_cuidado.cuidado
    notificacionesModel.mensaje = historial_cuidado.descripcion

    thread = threading.Thread(target=notificaciones.enviarCorreo, args=(notificacionesModel,))
    thread.start()
    hilos.append(thread)

    #Posiblemente quitarlo
    for hilo in hilos:
        hilo.join()

@historialCuidados.put("/", response_model=HistorialCuidadosSchema)
def update_historial_Cuidados(historialCuidados: HistorialCuidadosSchema):
    historialCuidado = session.query(historialCuidadosModel).filter_by(id = historialCuidados.id).one()

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
        raise HTTPException(status_code=404, detail="historial de signo vital no encontrado")
    
    return historialCuidado


@historialCuidados.delete("/")
def delete_historial_cuidado(idregistro: int):
    historialCuidado = session.query(historialCuidadosModel).filter(historialCuidadosModel.id== idregistro).one()

    if historialCuidado:
        session.delete(historialCuidado)
        session.commit()
        return {"mensaje": "historial cuidado Eliminado"}
    
    else:
        raise HTTPException(status_code=404, detail="historial cuidado no encontrado")

