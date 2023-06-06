import sys
sys.path.append("..")
from fastapi import APIRouter, Depends
from utils.db import DataBaseConnection
from utils.dbAlchemy import session
from schema.PersonalMedico import PersonalMedicoSchema, PersonalMedicoBase
from sqlalchemy.orm import Session
from typing import List
from models.model import PersonalMedicoModel




personalMedico = APIRouter()

@personalMedico.get("/all/", response_model=List[PersonalMedicoSchema])
async def listar_personalmedico():
    medicos = session.query(PersonalMedicoModel).all()
    return medicos

@personalMedico.get("/{id}", response_model=PersonalMedicoSchema)
async def obtenerMedicoPorUsuario(id: int):
    medico = session.query(PersonalMedicoModel).filter_by(usuario_id=id).first()
    return medico
