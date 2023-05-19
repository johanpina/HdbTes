import sys
sys.path.append("..")
import psycopg2
from fastapi import APIRouter, File
from os import getcwd
from schema.PersonalMedico import PersonalMedico
from utils.db import DataBaseConnection
from fastapi import FastAPI
from fastapi.responses import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from pathlib import Path
from utils.dbAlchemy import session
from models.FamiliarDesignado import FamiliarDesignadoModel
from models.Paciente import PacienteModel
from models.Usuario import UsuarioModel

conn = DataBaseConnection()
paciente = APIRouter()
cur = conn.cursor()

@paciente.get("/all/")
def listar_allUsers():
    cur.execute("SELECT * FROM paciente")
    for data in cur:
        print(data)


@paciente.get("/pacientesporfamiliar")
def listar_pacientesporfamiliar(idfamiliar: int):
    PacientesAcargo = session.query(FamiliarDesignadoModel, PacienteModel, UsuarioModel).join(PacienteModel, FamiliarDesignadoModel.id== PacienteModel.familiar_id).join(UsuarioModel, PacienteModel.usuario_id == UsuarioModel.id).filter(FamiliarDesignadoModel.id == idfamiliar).all()
    resultado_json = []
    for item in PacientesAcargo:
        tabla_data = item[2].__dict__
        resultado_json.append({
            key: value for key, value in tabla_data.items() if not key.startswith('_')
        })
    return resultado_json   

