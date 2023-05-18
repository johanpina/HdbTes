import sys
sys.path.append("..")

from fastapi import APIRouter, HTTPException
from utils.dbAlchemy import session
from models.SignosVitales import signosVitalesModel
from schema.SignosVitales import SignosVitalesSchema



signosVitales = APIRouter()

@signosVitales.get("/all/")
def get_signosVitales():
    Signos = session.query(signosVitalesModel).all()
    return Signos

@signosVitales.post("/")
def create_signosVitales(signosVitales: SignosVitalesSchema):
    new_signoVital = signosVitalesModel(id=signosVitales.id ,nombre_signo= signosVitales.nombre_signo, unidad= signosVitales.unidad)
    result = session.add(new_signoVital)
    session.commit()
    return result

@signosVitales.put("/")
def update_signosVitales(signosVitales: SignosVitalesSchema):
    signovital = session.query(signosVitalesModel).filter_by(id = signosVitales.id).first()

    if signovital:

        signovital.nombre_signo = signosVitales.nombre_signo
        signovital.unidad = signosVitales.unidad
        session.commit()
        print("Registro Actualizado exitosamente")
    
    else:
        print("No se encontro el registro con el ID proporcionado.")

@signosVitales.delete("/")
def delete_signoVital(idregistro: int):
    signovital = session.query(signosVitalesModel).filter_by(id = idregistro).first()

    if signovital:
        session.delete(signovital)
        session.commit()
        print("Registro eliminado exitosamente")
    
    else:
        print("No se encontro el registro con el ID proporcionado")