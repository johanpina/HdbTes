from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from router.Usuario import user
from router.PersonalMedico import personalMedico
from router.HistorialDiagnostico import historialDiagnostico
from router.Paciente import paciente
from router.FamiliarDesignado import familiarDesignado
from services.login import login
from router.HistorialCuidados import historialCuidados
from router.SignosVitales import signosVitales
from router.HistorialSignoVital import historialSignosVital
from router.PersonalACargo import personalAcargo
from fastapi.middleware.cors import CORSMiddleware
from utils.dbAlchemy import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:5173",
    "https://delightful-plant-0a1f3470f.3.azurestaticapps.net",
    "https://190.165.114.93,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user, prefix='/user')
app.include_router(personalMedico, prefix='/personalMedico')
app.include_router(historialDiagnostico, prefix='/historialDiagnostico')
app.include_router(paciente, prefix='/paciente')
app.include_router(familiarDesignado, prefix='/familiarDesignado')
app.include_router(login, prefix='/login')
app.include_router(historialCuidados, prefix='/cuidados')
app.include_router(signosVitales, prefix='/signosVitales')
app.include_router(historialSignosVital, prefix='/historialsignosvitales')
app.include_router(personalAcargo, prefix='/personalAcargo')

@app.get("/")
def hello_world():
    return {"message": "Servidor ejecutandose"}


