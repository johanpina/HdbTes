import sys
sys.path.append("..")
import psycopg2

from fastapi import APIRouter
from schema.Usuario import Usuario
from utils.db import DataBaseConnection, run_query

conn = DataBaseConnection()


user = APIRouter()


@user.get("/all/")
def listar_allUsers():
    cur = run_query("SELECT * FROM Usuario")
    for data in cur:
        print(data)