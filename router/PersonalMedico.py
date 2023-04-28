import sys
sys.path.append("..")
import psycopg2
#import pandas as pd
#import openpyxl
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
personalMedico = APIRouter()
cur = conn.cursor()


@personalMedico.get("/all/")
def listar_personalMedico():
    print("jenicjen")
    cur.execute("SELECT * FROM personalMedico")
    for data in cur:
        print(data)

@personalMedico.get("/historiaClinicaPaciente/{id}")
def listarHistoriaClinicaPaciente(id:int):
    listaHistorialDiagnostico = []

    cur.execute("""SELECT uspa.nombre, uspa.apellido, uspa.cedula, uspa.edad, hd.fecha, di.descripcion, us.nombre, 
                          pm.tarjeta_profesional, pm.especialidad, pm.tipo_personal FROM historialDiagnostico hd
                   INNER JOIN personalMedico pm on hd.medico_Id = pm.id 
                   INNER JOIN usuario us on pm.usuario_Id = us.id
                   INNER JOIN paciente pa on hd.paciente_Id = pa.id
                   INNER JOIN usuario uspa on pa.usuario_id = uspa.id
                   INNER JOIN familiarDesignado fd on pa.familiar_Id = fd.id
                   INNER JOIN usuario usfd on fd.usuario_Id = usfd.id
                   INNER JOIN diagnostico di on hd.diagnostico_Id = di.id
                   where paciente_id='%s'; """% id)

    rows = cur.fetchall()
    
    pdf_canvas = canvas.Canvas("historial_clinico.pdf", pagesize=letter)

    x = 40
    y = 690

    # Dibujar la cabecera con la información de la clínica
    pdf_canvas.setFont('Helvetica-Bold', 16)
    pdf_canvas.drawString(x*6, 750, "Clinica CodeLabs")
    pdf_canvas.setFont('Helvetica', 12)
    pdf_canvas.drawString(x*4.5, 735, "Dirección: Calle 65 No 26 - 10, Manizales Caldas")
    pdf_canvas.drawString(x*6, 720, "Teléfono: 8000-512120")
    pdf_canvas.line(36,710,576,710)

    for tupla in rows:
        pdf_canvas.drawString(x, y, "Nombre Paciente: " + str(tupla[0]))
        pdf_canvas.drawString(x, y-20, "Apellido Paciente: "+ str(tupla[1]))
        pdf_canvas.drawString(x, y-40, "Cedula: "+ str(tupla[2]))
        pdf_canvas.drawString(x, y-60, "Edad: " + str(tupla[3]))
        pdf_canvas.drawString(x, y-80, "Fecha: " + str(tupla[4]))
        pdf_canvas.drawString(x, y-100, "Motivo de consulta: " + tupla[5])
        pdf_canvas.drawString(x, y-120, "Doctor: " + tupla[6])
        pdf_canvas.drawString(x, y-140, "Tarjeta profesional: " + str(tupla[7]))
        pdf_canvas.drawString(x, y-160, "Especialidad: " + tupla[8])
        pdf_canvas.drawString(x, y-180, "Tipo de personal médico: " + tupla[9])
        y -= 220

    pdf_canvas.save()
    pdf_name = "historial_clinico.pdf"
    pdf_path = Path.cwd() / pdf_name
    headers = {"Content-Disposition": f"attachment; filename={pdf_name}"}
    #return FileResponse(pdf_path, headers=headers, media_type="application/pdf")

    for data in rows:
        listaHistorialDiagnostico.append(data)
    return  {"message": listaHistorialDiagnostico}


@personalMedico.get('/download/{nombre_archivo}')
def descargarHistorial(nombre_archivo:str):
    return FileResponse(getcwd() +"/"+ nombre_archivo, media_type="application/octet-stream", filename=nombre_archivo)