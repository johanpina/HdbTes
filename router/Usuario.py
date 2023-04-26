import sys
sys.path.append("..")
import psycopg2

from fastapi import APIRouter
from schema.Usuario import Usuario
from utils.db import DataBaseConnection

conn = DataBaseConnection()


user = APIRouter()

cur = conn.cursor()


@user.get("/all/")
def listar_allUsers():
    cur.execute("SELECT * FROM Usuario")
    for data in cur:
        print(data)
   