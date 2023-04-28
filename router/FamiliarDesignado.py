import sys
sys.path.append("..")
import psycopg2
from fastapi import APIRouter
from schema.Usuario import Usuario
from utils.db import DataBaseConnection

conn = DataBaseConnection()
familiarDesignado = APIRouter()
cur = conn.cursor()


@familiarDesignado.get("/all/")
def listar_allFamiliarDesignado():
    cur.execute("SELECT * FROM Usuario")
    for data in cur:
        print(data)