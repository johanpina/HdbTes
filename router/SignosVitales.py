import sys
sys.path.append("..")

from fastapi import APIRouter, HTTPException
from utils.db import DataBaseConnection, run_query
#from utils.dbAlchemy import conn

#--------
from utils.dbAlchemy import session
from models.SignosVitales import signosVitalesModel



signosVitales = APIRouter()
#cur = conn.cursor()

@signosVitales.get("/all/")
def get_signosVitales():
    historialSignos = session.query(signosVitalesModel).all()
    return historialSignos