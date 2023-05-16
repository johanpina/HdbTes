import sys
sys.path.append("..")
import psycopg2

from fastapi import APIRouter, HTTPException
from utils.db import DataBaseConnection, run_query
#from utils.dbAlchemy import conn

#--------
from utils.dbAlchemy import session
from models.HistorialCuidados import historialCuidadosModel
from sqlalchemy import func, select


historialCuidados = APIRouter()
#cur = conn.cursor()

@historialCuidados.get("/all/")
def get_historialCuidados():
    historiales = session.query(historialCuidadosModel).all()
    return historiales

# conn.execute(historialCuidados.select()).fetchall()