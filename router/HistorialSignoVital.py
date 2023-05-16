import sys
sys.path.append("..")

from fastapi import APIRouter, HTTPException
from utils.db import DataBaseConnection, run_query
#from utils.dbAlchemy import conn

#--------
from utils.dbAlchemy import session
from models.HistorialSignosVital import historialSignosVitalModel



historialSignosVital = APIRouter()
#cur = conn.cursor()

@historialSignosVital.get("/all/")
def get_historialSignosVital():
    historialSignos = session.query(historialSignosVitalModel).all()
    return historialSignos