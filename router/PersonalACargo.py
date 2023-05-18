import sys
sys.path.append("..")
import psycopg2

from fastapi import APIRouter, HTTPException
from schema.PersonalACargo import PersonalACargoSchema
from utils.dbAlchemy import session
from models.PersonalACargo import PersonalACargoModel
from models.Paciente import PacienteModel
from models.Usuario import UsuarioModel

personalAcargo = APIRouter()


@personalAcargo.get("/all/")
def get_allPersonalAcargo():
    PersonalesACargo = session.query(PersonalACargoModel).all()
    return PersonalesACargo

@personalAcargo.post("/")
def create_PersonalAcargo(personalAcargo: PersonalACargoSchema):
    new_personalAcargo = PersonalACargoModel(id=personalAcargo.id ,medico_id= personalAcargo.medico_id, paciente_id= personalAcargo.paciente_id, paciente_activo = personalAcargo.paciente_activo)
    result = session.add(new_personalAcargo)
    session.commit()
    return result

@personalAcargo.put("/")
def update_PersonalAcargo(personalAcargo: PersonalACargoSchema):
    personalac = session.query(PersonalACargoModel).filter_by(id = personalAcargo.id).first()

    if personalac:

        personalac.medico_id = personalAcargo.medico_id
        personalac.paciente_id = personalAcargo.paciente_id
        personalac.paciente_activo = personalAcargo.paciente_activo

        session.commit()
        print("Registro Actualizado exitosamente")
    
    else:
        print("No se encontro el registro con el ID proporcionado.")

@personalAcargo.delete("/")
def delete_personalAcargo(idregistro: int):
    personal = session.query(PersonalACargoModel).filter_by(id = idregistro).first()

    if personal:
        session.delete(personal)
        session.commit()
        print("Registro eliminado exitosamente")
    
    else:
        print("No se encontro el registro con el ID proporcionado")

@personalAcargo.get("/pacientes")
def get_allPersonalAcargo(idmedico: int):
    PersonalesACargo = session.query(PersonalACargoModel, PacienteModel, UsuarioModel).join(PacienteModel, PersonalACargoModel.paciente_id== PacienteModel.id).join(UsuarioModel, PacienteModel.usuario_id == UsuarioModel.id).filter(PersonalACargoModel.medico_id == idmedico).all()
    resultado_json = []
    for item in PersonalesACargo:
        tabla_data = item[2].__dict__
        resultado_json.append({
            key: value for key, value in tabla_data.items() if not key.startswith('_')
        })

    # Retornar los resultados en formato JSON
    return resultado_json