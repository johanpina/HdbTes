import sys
sys.path.append("..")
import psycopg2

from fastapi import APIRouter, HTTPException
from utils.db import DataBaseConnection, run_query
#from utils.dbAlchemy import conn

#--------
from utils.dbAlchemy import session
from models.HistorialCuidados import historialCuidadosModel
from models.Paciente import PacienteModel
from models.Usuario import UsuarioModel
from models.notificaciones import notificacionesModel
from models.FamiliarDesignado import FamiliarDesignadoModel
from schema.HistorialCuidados import HistorialCuidadosSchema
from sqlalchemy import func, select
from services import notificaciones
import threading 


historialCuidados = APIRouter()
#cur = conn.cursor()

@historialCuidados.get("/all/")
def get_historialCuidados():
    historiales = session.query(historialCuidadosModel).all()
    return historiales

@historialCuidados.post("/")
def create_historial_cuidados(historialCuidados: HistorialCuidadosSchema):
    hilos = []
    new_historial_Cuidado = historialCuidadosModel(  id = historialCuidados.id,
                                                     fecha_inicial=historialCuidados.fecha_inicial, 
                                                     fecha_final=historialCuidados.fecha_final,
                                                     cuidado=historialCuidados.cuidado,
                                                     medico_id=historialCuidados.medico_id,
                                                     paciente_id=historialCuidados.paciente_id,
                                                     descripcion=historialCuidados.descripcion)
    result = session.add(new_historial_Cuidado)
    session.commit()

    paciente = session.query(PacienteModel).filter(PacienteModel.id == new_historial_Cuidado.paciente_id).first()
    familiarDesignado = session.query(FamiliarDesignadoModel).filter(FamiliarDesignadoModel.id == paciente.familiar_id).first()
    usuario = session.query(UsuarioModel).filter(UsuarioModel.id == familiarDesignado.usuario_id).first()

    notificacionesModel.destino = usuario.email
    notificacionesModel.asunto = new_historial_Cuidado.cuidado
    notificacionesModel.mensaje = new_historial_Cuidado.descripcion

    thread = threading.Thread(target=notificaciones.enviarCorreo, args=(notificacionesModel,))
    thread.start()
    hilos.append(thread)

    #Posiblemente quitarlo
    for hilo in hilos:
        hilo.join()

    return result


@historialCuidados.put("/")
def update_historial_Cuidados(historialCuidados: HistorialCuidadosSchema):
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