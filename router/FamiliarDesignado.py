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

conn = DataBaseConnection()
familiarDesignado = APIRouter()
cur = conn.cursor()


@familiarDesignado.get("/all/")
def listar_allFamiliarDesignado():
    cur.execute("SELECT * FROM familiardesignado")
    for data in cur:
        print(data)
