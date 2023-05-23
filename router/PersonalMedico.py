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
