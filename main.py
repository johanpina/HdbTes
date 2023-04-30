from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from router.Usuario import user
from router.PersonalMedico import personalMedico
from router.HistorialDiagnostico import historialDiagnostico
from router.Paciente import paciente
from router.FamiliarDesignado import familiarDesignado
from services.login import login


app = FastAPI()



app.include_router(user, prefix='/user')
app.include_router(personalMedico, prefix='/personalMedico')
app.include_router(historialDiagnostico, prefix='/historialDiagnostico')
app.include_router(paciente, prefix='/paciente')
app.include_router(familiarDesignado, prefix='/familiarDesignado')
app.include_router(login, prefix='/login')

@app.get("/")
def hello_world():
    return {"message": "Servidor ejecutandose"}


